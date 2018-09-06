from budgets.lib.budget_query import BudgetQuery
from budgets.serializers.budget_serializer import BudgetSerializer
from rest_framework import views, exceptions
from rest_framework.response import Response

# Create your views here.
class AllBudgetList(views.APIView):

    def get(self, request):
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if year is not None and month is not None:
            quert_data = BudgetQuery(year, month).all_budget()
            results = BudgetSerializer(quert_data, many = True).data
            return Response(results)
        else:
            raise exceptions.ParseError("month or year no correctly provided")
