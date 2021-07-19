from rest_framework import status
from rest_framework.generics import get_object_or_404,GenericAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.views import APIView
from core.models import CarModel
from .serializers import CarSerializer


# class CarCreateListView(GenericAPIView, ListModelMixin, CreateModelMixin):
class CarCreateListView(ListCreateAPIView):
    serializer_class = CarSerializer
        
    # queryset = CarModel.objects.all()

    def get_queryset(self):
        qs = CarModel.objects.all()
        params = self.request.query_params
        get = params.get('brand_start', None)
        brand_start = params.get('brand_start', None)
        if brand_start:
            qs = qs.filter(brand__istartswith=brand_start)
        return qs
    # def get(self, *args, **kwargs):
    #     qs = CarModel.objects.all()
    #     serializer = CarSerializer(qs, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
    # 
    # def post(self, *args, **kwargs):
    #     body = self.request.data
    #     serializer = CarSerializer(data=body)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveDeleteView(APIView):
    serializer_class = CarSerializer
    queryset = CarModel
    
    # def get(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     data = get_object_or_404(CarModel, pk=pk)
    #     # try:
    #     #     data = CarModel.objects.get(pk=pk)
    #     # except Exception as e:
    #     #     return Response('Not Found', status.HTTP_404_NOT_FOUND)
    #     serializer = CarSerializer(data)
    #     return Response(serializer.data, status.HTTP_200_OK)
    # 
    # def put(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     body = self.request.data
    #     try:
    #         data = CarModel.objects.get(pk=pk)
    #     except Exception:
    #         return Response('Not Found', status.HTTP_404_NOT_FOUND)
    #     serializer = CarSerializer(data, data=body)
    #     serializer.is_valid(raise_exception=True)
    #     # if not serializer.is_valid():
    #     #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    #     serializer.save()
    #     return Response(serializer.data,status.HTTP_202_ACCEPTED)
    # 
    # def patch(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     body = self.request.data
    #     try:
    #         data = CarModel.objects.get(pk=pk)
    #     except Exception:
    #         return Response('Not Found', status.HTTP_404_NOT_FOUND)
    #     serializer = CarSerializer(data, data=body, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_202_ACCEPTED)
    # 
    # def delete(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     try:
    #         data = CarModel.objects.get(pk=pk)
    #     except Exception as e:
    #         return Response('Not Found', status.HTTP_404_NOT_FOUND)
    #     data.delete()
    #     return Response('delete', status.HTTP_204_NO_CONTENT)


# class TestApi(APIView):
#     def get(self, *args, **kwargs):
#         qs = CarModel.objects.all()
#         lt = self.request.query_params.get('lt', None)
#         if lt:
#             qs = qs.filter(year__lt=lt)
#
#         serializer = CarSerializer(qs, many=True)
#
#         return Response(serializer.data)
