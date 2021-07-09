import datetime
from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField(min_value=1900, max_value=datetime.date.today().year)
    brand = serializers.CharField(validators=[
        RegexValidator('^[a-zA-Z]{2,20}$', 'only alpha min 2ch max 20ch')
    ])

    class Meta:
        model = CarModel
        fields = '__all__'

    def validate_year(self, year):
        if year % 2 == 0:
            raise serializers.ValidationError('only odd years')
        return year
    def validate(self, attrs):
        print(attrs)
        return attrs
