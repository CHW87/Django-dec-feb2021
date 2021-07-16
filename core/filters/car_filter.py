from django_filters import rest_framework as filters

from core.models import CarModel


class CarFilter(filters.FilterSet):
    brand = filters.CharFilter()
    year = filters.RangeFilter()
    user = filters.BaseInFilter(field_name='userId')

    class Meta:
        model = CarModel
        fields = ('brand', 'year', 'user')
