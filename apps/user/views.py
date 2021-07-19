from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.contrib.auth.models import User

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
	serializer_class = UserSerializer
	queryset = UserModel.objects.all()


class RetrieveDeleteView(RetrieveUpdateDestroyAPIView):
	serializer_class = UserSerializer
	queryset = UserModel
