from budgets.serializers.budget_sum_serializer import BudgetSumSerializer
from budgets.lib.budget_query import BudgetQuery
from rest_framework import exceptions, generics
from budgets.lib.auth import TokenAuthentication

# Create your views here.
class MonthlyBudgetSumList(generics.ListCreateAPIView):

    serializer_class = BudgetSumSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        request = self.request
        username = self.request.user.username
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        if year is not None and month is not None:
            self.queryset = BudgetQuery(year, month, username).monthly_budget_sum()
            return self.queryset
        else:
            raise exceptions.ParseError("month or year no correctly provided")
