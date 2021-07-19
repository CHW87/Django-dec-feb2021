from django.urls import path
from .views import CarCreateListView, RetrieveDeleteView

urlpatterns = [
    path('', CarCreateListView.as_view(), name='car_list_create'),
    path('/<int:pk>', RetrieveDeleteView.as_view(), name='car_retrieve_delete'),
]
