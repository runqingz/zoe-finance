from budgets.serializers.budget_sum_serializer import BudgetSumSerializer
from budgets.lib.budget_query import BudgetQuery
from rest_framework import views, exceptions
from rest_framework.response import Response

# Create your views here.
class MonthlyBudgetSumList(views.APIView):

    def get(self, request):
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if year is not None and month is not None:
            query_data = BudgetQuery(year, month).monthly_budget_sum()
            results = BudgetSumSerializer(query_data, many=False).data
            return Response(results)
        else:
            raise exceptions.ParseError("month or year no correctly provided")

