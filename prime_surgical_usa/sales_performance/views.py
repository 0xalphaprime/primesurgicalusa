from django.shortcuts import render
from .gsheets import get_google_sheet_data  # Import the function that pulls data from Google Sheets
from .gsheets_item_class_rolling_qtr import gsheet_data_item_class_rolling_qtr
import pandas as pd

# Create your views here.

# this was our first one here, not optimally named. this is our daily sales
def sheet_data_view(request):
    # Fetch the data from Google Sheets
    data = get_google_sheet_data()

    # Pass the data to the template context
    return render(request, 'sales_performance/zb_sales_dash.html', {'data': data})

def item_class_rolling_qtr(request):
    # Fetch the data from Google Sheets & convert to pandas dataframe
    incoming_data = gsheet_data_item_class_rolling_qtr()
    df = pd.DataFrame(incoming_data)

    # remove dollar sign from net sales and sales price
    df['Net Sales Amount'] = df['Net Sales Amount'].replace('[\$,]', '', regex=True).astype(float)
    df['Sale Price'] = df['Sale Price'].replace('[\$,]', '', regex=True).astype(float)

    #convert calendar date
    df['Calendar Date'] = pd.to_datetime(df['Calendar Date'])


    # Generate the pivot table
    pivot_table = pd.pivot_table(df, values='Net Sales Amount', 
                                 index=r'Calendar Year\Quarter', 
                                 columns='Item Class', 
                                 aggfunc='sum', fill_value=0)

    # Filter out columns that contain only zeros
    pivot_table = pivot_table.loc[:, (pivot_table != 0).any(axis=0)]

    # Remove the 'OTH_Other' column if it exists
    if 'OTH_Other' in pivot_table.columns:
        pivot_table = pivot_table.drop(columns=['OTH_Other'])

    # Add a 'Total' column that sums each row (i.e., each quarter)
    pivot_table['Total'] = pivot_table.sum(axis=1)

    # Add percentage columns for each item class
    percentage_columns = pivot_table.div(pivot_table['Total'], axis=0) * 100
    percentage_columns = percentage_columns.drop(columns=['Total'])  # Remove 'Total' from the percentage calculation

    # Rename percentage columns to indicate they are percentages
    percentage_columns = percentage_columns.add_suffix(' %')

    # Combine the original pivot table with the percentage columns
    combined_pivot_table = pd.concat([pivot_table, percentage_columns], axis=1)

    # Format the values as currency and percentages, explicitly converting to strings
    combined_pivot_table.iloc[:, :pivot_table.shape[1]] = combined_pivot_table.iloc[:, :pivot_table.shape[1]].apply(lambda x: x.map('${:,.2f}'.format).astype(str))
    combined_pivot_table.iloc[:, pivot_table.shape[1]:] = combined_pivot_table.iloc[:, pivot_table.shape[1]:].apply(lambda x: x.map('{:.2f}%'.format).astype(str))

    # Convert the DataFrame to HTML
    pivot_table_html = combined_pivot_table.to_html(classes='table table-striped', index=True, border=0)

    # Pass the HTML to the template
    return render(request, 'sales_performance/zb_sales_item_class_qtr_rolling.html', {'pivot_table_html': pivot_table_html})

def index(request):
    return render(request, 'sales_performance/sales_performance.html')

def zb_sales_dashboard(request):
    return render(request, 'sales_performance/zb_sales_dash.html')