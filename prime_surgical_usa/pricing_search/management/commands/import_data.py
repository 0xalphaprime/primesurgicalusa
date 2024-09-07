# this file is used to import data from an Excel file into the database.
# first, it clears all existing data in the PriceRecord table.
# then, it reads the data from the Excel file and creates or updates PriceRecord objects in the database.
# it also prints the number of records processed, created, and updated.
#
# pricing_search/management/commands/import_data.py
import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from pricing_search.models import PriceRecord

class Command(BaseCommand):
    help = 'Import data from Excel file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            # Clear existing data
            PriceRecord.objects.all().delete()

            # Load the Excel file
            df = pd.read_excel(file_path)

            # Check required columns in DataFrame
            required_columns = {'Item Number', 'Account Name', 'Price', 'Description'}
            if not required_columns.issubset(df.columns):
                raise CommandError(f'Missing required columns: {required_columns - set(df.columns)}')

            records_processed = 0
            records_updated = 0
            records_created = 0

            for index, row in df.iterrows():
                item_number = str(row['Item Number']).strip()
                account_name = str(row['Account Name']).strip()
                price = row['Price']
                description = str(row['Description']).strip()

                price_record, created = PriceRecord.objects.update_or_create(
                    item_number=item_number,
                    account_name=account_name,
                    defaults={
                        'price': price,
                        'description': description,
                    }
                )

                if created:
                    records_created += 1
                else:
                    records_updated += 1

                records_processed += 1

            self.stdout.write(self.style.SUCCESS(f"Successfully processed {records_processed} records"))
            self.stdout.write(self.style.SUCCESS(f"Created {records_created} new records"))
            self.stdout.write(self.style.SUCCESS(f"Updated {records_updated} existing records"))
        except Exception as e:
            raise CommandError(f'Error importing data: {e}')