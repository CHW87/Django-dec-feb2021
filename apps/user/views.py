from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import UserSerializer, UserUpdateSerializer
from apps.car.serializers import CarByUserIdSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserUpdateSerializer
    queryset = UserModel.objects.all()


class AddCarByUserIdView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = CarByUserIdSerializer
    queryset = UserModel

    def perform_create(self, serializer):
        print(self.request.user.__dict__)
        serializer.save(user=self.get_object())
