from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ComputerModel
from .serializers import ComputerSerializer


# Create your views 


class ComputerCreateListView(APIView):

	def get(self, *args, **kwargs):
		qs = ComputerModel.objects.all()
		serializer = ComputerSerializer(qs, many=True)
		return Response(serializer.data)

	def post(self, *args, **kwargs):
		body = self.request.data
		serializer = ComputerSerializer(data=body)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveDeleteView(APIView):
	def get(self, *args, **kwargs):
		pk = kwargs.get('pk')
		data = get_object_or_404(ComputerModel, pk=pk)
		# try:
		# 	data = ComputerModel.objects.get(pk=pk)
		# except Exception as e:
		# 	return Response('Not Found')
		serializer = ComputerSerializer(data)
		return Response(serializer.data, status.HTTP_200_OK)

	def put(self, *args, **kwargs):
		pk = kwargs.get('pk')
		body = self.request.data
		try:
			data = ComputerModel.objects.get(pk=pk)
		except ComputerModel.DoesNotExist:
			return Response('Not Found', status.HTTP_404_NOT_FOUND)
		serializer = ComputerSerializer(data, data=body)
		serializer.is_valid(raise_exception=True)
		# if not serializer.is_valid():
		#     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
		serializer.save()
		return Response(serializer.data, status.HTTP_202_ACCEPTED)

	def patch(self, *args, **kwargs):
		pk = kwargs.get('pk')
		body = self.request.data
		try:
			data = ComputerModel.objects.get(pk=pk)
		except Exception:
			return Response('Not found', status.HTTP_404_NOT_FOUND)
		serializer = ComputerSerializer(data, data=body, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status.HTTP_202_ACCEPTED)

	def delete(self, *args, **kwargs):
		pk = kwargs.get('pk')
		try:
			data = ComputerModel.objects.get(pk=pk)
		except Exception as e:
			return Response('Not Found', status.HTTP_404_NOT_FOUND)
		data.delete()
		return Response('deleted', status.HTTP_204_NO_CONTENT)
