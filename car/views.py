# from django.shortcuts import render
#
# cars = [
#     {"model": 'BMW', "year": 2020},
#     {"model": 'Audi', "year": 2010},
#     {"model": 'KIA', "year": 2008},
# ]
#
#
# # Create your views here.
# def home(request):
#     return render(request, 'index.html', {"cars": cars})
#
#
# def add_car(request, year, model):
#     cars.append({'model':model, 'year':year})
#     return render(request, 'index.html', {"cars": cars})


# class MyView(APIView):
#     def get(self, *args, **kwargs):
#         params = self.request.query_params
#         name = params.get('name')
#         print(name)
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
# class MyViewSecond(APIView):
#     def get(self, *args,**kwargs):
#         print(kwargs.get('id'))
#         return Response('Ok')
# localhost:8000/cars/create
# localhost:8000/cars/delete

"""
Create
Read
Update
Delete
"""

# lh:8000/cars GET all
# lh:8000/cars POST create
# lh:8000/cars/:id GET get one
# lh:8000/cars/:id PUT update all
# lh:8000/cars/:id PATCH update few fields
# lh:8000/cars/:id DELETE delete item
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarModel
from .serializers import CarSerializer


class CarCreateListView(APIView):
    def get(self, *args, **kwargs):
        qs = CarModel.objects.all()
        serializer = CarSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        body = self.request.data
        serializer = CarSerializer(data=body)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class RetriaveDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = CarModel.objects.get(pk=pk)
        except Exception as e:
            return Response('Not Found')
        serializer = CarSerializer(data)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = CarModel.objects.get(pk=pk)
        except Exception as e:
            return Response('Not Found')
        data.delete()
        return Response('delete')
