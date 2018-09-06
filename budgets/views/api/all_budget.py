from budgets.serializers.budget_serializer import BudgetSerializer
from budgets.lib.budget_query import BudgetQuery
from rest_framework import exceptions, generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AllBudgetList(generics.ListCreateAPIView):

    serializer_class = BudgetSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        request = self.request
        user = self.request.user
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        if year is not None and month is not None:
            self.queryset = BudgetQuery(year, month, user).all_budget()
            return self.queryset
        else:
            raise exceptions.ParseError("month or year no correctly provided")
