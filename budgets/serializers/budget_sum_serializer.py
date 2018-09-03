from rest_framework import serializers
from budgets.models.budget import Budget

class BudgetSumSerializer (serializers.Serializer):
    amount__sum = serializers.IntegerField()

