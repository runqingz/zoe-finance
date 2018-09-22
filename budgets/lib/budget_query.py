from budgets.models.budget import Budget
from django.db.models import Sum

class BudgetQuery:

    def __init__(self, year, month, username):
        self.year = year
        self.month = month
        self.username = username

    def all_budget(self):
        return Budget.objects.filter(user__username=self.username)

    def monthly_budget(self):
        return Budget.objects.filter(date__year=self.year,
                                     date__month=self.month,
                                     user__username=self.username)

    def monthly_budget_sum(self):
        return Budget.objects.filter(date__year=self.year,
                                     date__month=self.month,
                                     user__username=self.username).annotate(amount_sum=Sum('amount'))

