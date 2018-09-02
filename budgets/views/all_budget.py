from budgets.lib.budget_query import BudgetQuery
from budgets.serializers.budget_serializer import BudgetSerializer
from rest_framework import generics

# Create your views here.
class AllBudgetsListCreate(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        month = self.request.query_params.get('month')

        if year is not None and month is not None:
            return BudgetQuery(year, month).all_budget()
        else:
            raise exceptions.ParseError("month or year no correctly provided")
