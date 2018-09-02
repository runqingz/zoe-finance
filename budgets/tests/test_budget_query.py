from django.test import TestCase
from budgets.lib.budget_query import BudgetQuery
from budgets.models.budget import Budget
from datetime import datetime
from datetime import timedelta

class BudgetApiTestCases(TestCase):
    def setUp(self):
        sep_date = datetime(2010,9,10,18,00)
        aug_date = datetime(2010,8,10,18,00)
        for x in range(0,3):
            Budget.objects.create(amount=x,
                                  date=sep_date+timedelta(days=x),
                                  category='FO',
                                  description = 'some expense')
            Budget.objects.create(amount=x,
                                  date=aug_date+timedelta(days=(x+1)),
                                  category='FO',
                                  description = 'some expense')
# Create your tests here.
    def test_all_budget_result(self):
        query_result = BudgetQuery(2010, 9).all_budget()
        self.assertEqual(query_result.count(), 6)
