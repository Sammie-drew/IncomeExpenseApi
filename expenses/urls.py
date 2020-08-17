from django.urls import path
from .views import *

urlpatterns = [
    path("", ExpenseListApiView.as_view(), name="expenses"),
    path("<int:id>", ExpenseDetailApiView.as_view(), name="expense-details")
]
