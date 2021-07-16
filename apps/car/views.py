from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from core.models import CarModel
from .serializers import CarSerializer
from core.paginaions.car_paninator import CarPaginator
from core.filters.car_filter import CarFilter


class CarCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CarSerializer
    pagination_class = CarPaginator
    filterset_class = CarFilter

    def get_queryset(self):
        qs = CarModel.objects.all()
        params = self.request.query_params
        user_id = params.get('userId', None)
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs


class RetriaveDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel
    lookup_field = 'id'
