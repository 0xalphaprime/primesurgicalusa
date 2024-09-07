# this file contains the model for the PriceRecord table in the database
# the model has fields for item number, account name, price, unit of measure, and description


# pricing_search/models.py
from django.db import models

class PriceRecord(models.Model):
    item_number = models.CharField(max_length=50)
    account_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        unique_together = ('item_number', 'account_name')

    def __str__(self):
        return f"{self.item_number} - {self.account_name}"