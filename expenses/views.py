from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from expenses.models import Expense
from expenses.serializers import ExpensesSerializer


# or we can use viewsets, the same thing but with just 1 class
class ExpensesListView(ListCreateAPIView):
    queryset = Expense.objects.order_by('-date')
    serializer_class = ExpensesSerializer


class ExpenseView(RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpensesSerializer
