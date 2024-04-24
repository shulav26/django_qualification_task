from django.urls import path
from .views import ComputerListView, ComputerCreateView, ComputerUpdateView

urlpatterns = [
    path('list/', ComputerListView.as_view(), name='computer_list'),
    path('create/', ComputerCreateView.as_view(), name='computer_create'),
    path('update/<int:pk>/', ComputerUpdateView.as_view(), name='computer_update'),
]
