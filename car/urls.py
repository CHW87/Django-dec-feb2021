from django.urls import path

from .views import home, add_car
urlpatterns = [
    path('', home),
    path('/create/<int:year>/<str:model>/', add_car)

]
