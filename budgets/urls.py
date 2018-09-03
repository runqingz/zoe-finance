from django.urls import path

from .views import all_budget, monthly_budget, monthly_budget_sum

urlpatterns = [
    path('api/user/all', all_budget.AllBudgetList.as_view()),
    path('api/user/monthly', monthly_budget.MonthlyBudgetList.as_view()),
    path('api/user/monthly_sum', monthly_budget_sum.MonthlyBudgetSumList.as_view())
    ]
