from rest_framework import serializers

from expenses.models import Expense


class ExpensesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseSummarySerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()

    class Meta:
        model = Expense
        fields = ('category', 'number')
