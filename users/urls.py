from django.urls import path

from users import views


urlpatterns = [
    path('<int:pk>/expenses/', views.UserDateExpensesListView.as_view(), name='user-expenses'),
    path('<int:pk>/summary/', views.UserMonthSummaryExpensesListView.as_view(), name='user-summary')
]
