from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateDestroyView, AddCarByUserIdView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
    path('/<int:pk>/cars', AddCarByUserIdView.as_view(), name='user_add_car_by_user_id')
]
