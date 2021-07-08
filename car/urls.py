from django.urls import path
from .views import CarCreateListView, RetriaveDeleteView

urlpatterns = [
    path('', CarCreateListView.as_view(), name='car_list_create'),
    path('/<int:pk>', RetriaveDeleteView.as_view(), name='car_retriave_delete')
]
