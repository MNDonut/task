from django.urls import path

from expenses import views


urlpatterns = [
    path('', views.ExpensesListView.as_view(), name='expenses'),
    path('<int:pk>/', views.ExpenseView.as_view(), name='expense'),
]