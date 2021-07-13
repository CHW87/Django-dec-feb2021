from django.urls import path, include

urlpatterns = [
    path('/cars', include('apps.car.urls')),
    path('/users', include('apps.user.urls'))
]
