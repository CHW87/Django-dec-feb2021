from django.urls import path, include

urlpatterns = [
		path('/cars', include('apps.car.urls')),
		path('/users', include('apps.user.urls')),
		path('/computers', include('apps.computer.urls')),
]
