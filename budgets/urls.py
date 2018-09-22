from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views.api import all_budget, monthly_budget, monthly_budget_sum, \
        login, logout

urlpatterns = [
    path('api/all', all_budget.AllBudgetList.as_view()),
    path('api/monthly', monthly_budget.MonthlyBudgetList.as_view()),
    path('api/monthly_sum', monthly_budget_sum.MonthlyBudgetSumList.as_view()),
    path('api/login', obtain_jwt_token),
    path('api/logout', logout.Logout.as_view()),
    ]
