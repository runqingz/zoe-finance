from budgets.serializers.budget_serializer import BudgetSerializer
from budgets.lib.budget_query import BudgetQuery
from rest_framework import views, exceptions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.
class MonthlyBudgetList(views.APIView):

    def get(self, request):
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if year is not None and month is not None:
            query_data = BudgetQuery(year, month).monthly_budget()
            results = BudgetSerializer(query_data, many = True).data
            return Response(results)
        else:
            raise exceptions.ParseError("month or year no correctly provided")

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
