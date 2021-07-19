from django.urls import path
from .views import ComputerCreateListView, RetrieveDeleteView

urlpatterns = [
		path('', ComputerCreateListView.as_view(), name='computer_list_create'),
		path('/<int:id>', RetrieveDeleteView.as_view(), name='computer_retrieve_delete')
]

