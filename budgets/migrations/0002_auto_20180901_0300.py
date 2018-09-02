# Generated by Django 2.1.1 on 2018-09-01 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(choices=[('FO', 'Food'), ('CL', 'Clothing'), ('EL', 'Electronics'), ('GR', 'Grocery'), ('TR', 'Tranportation'), ('HR', 'Housing'), ('ED', 'Education'), ('ET', 'Entertainment'), ('OT', 'Other')], default='OT', max_length=2),
        ),
    ]