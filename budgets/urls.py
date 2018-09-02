from django.urls import path

from .views import all_budget, monthly_budget

urlpatterns = [
    path('api/user/all', all_budget.AllBudgetsListCreate.as_view()),
    path('api/user/monthly', monthly_budget.MonthlyBudgetsListCreate.as_view())
    ]
