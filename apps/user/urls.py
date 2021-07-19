from django.urls import path
from .views import UserListCreateView, RetrieveDeleteView

urlpatterns = [
		path('', UserListCreateView.as_view(), name='user_list_create'),
		path('/<int:id>', RetrieveDeleteView.as_view(), name='user_retrieve_delete')
]
