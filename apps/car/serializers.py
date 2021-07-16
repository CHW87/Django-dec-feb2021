import datetime
from rest_framework import serializers
from django.core.validators import RegexValidator
from core.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(min_value=1900, max_value=datetime.date.today().year)
    brand = serializers.CharField(validators=[
        RegexValidator('^[a-zA-Z]{2,20}$', 'only alpha min 2ch max 20ch')
    ])

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year', 'user')
        extra_kwargs = {
            'user': {"write_only": True}
        }


class CarByUserIdSerializer(CarSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model', 'year')
