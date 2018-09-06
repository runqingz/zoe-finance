from rest_framework import serializers
from budgets.models.budget import Budget

class BudgetSumSerializer (serializers.ModelSerializer):

    amount_sum = serializers.IntegerField()

    class Meta:
        model = Budget
        fields = ('amount_sum',)
