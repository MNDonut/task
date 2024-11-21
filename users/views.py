from django.contrib.auth import get_user_model
from django.db.models import Count

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from expenses.serializers import ExpensesSerializer, ExpenseSummarySerializer


class UserDateExpensesListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ExpensesSerializer

    def get(self, request, *args, **kwargs):
        expenses = self.get_object().expenses.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            expenses = expenses.filter(date__range=[start_date, end_date])
        
        expenses = expenses.order_by('-date')
        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)


class UserMonthSummaryExpensesListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ExpenseSummarySerializer

    def get(self, request, *args, **kwargs):
        expenses = self.get_object().expenses.all()
        month = self.request.query_params.get('month')
        if month:
            expenses = expenses.filter(date__month=month).values('category').annotate(number=Count('category'))
        else:
            expenses = expenses.values('category').annotate(number=Count('category'))

        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)
