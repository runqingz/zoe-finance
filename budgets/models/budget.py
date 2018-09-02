from django.db import models

# Create your models here.

class Budget(models.Model):
    CATEGORIES = (
        ('FO', 'Food'),
        ('CL', 'Clothing'),
        ('EL', 'Electronics'),
        ('GR', 'Grocery'),
        ('TR', 'Tranportation'),
        ('HR', 'Housing'),
        ('ED', 'Education'),
        ('ET', 'Entertainment'),
        ('OT', 'Other')
    )
    amount = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length = 100)
    category = models.CharField(max_length = 2, choices=CATEGORIES, default='OT')
