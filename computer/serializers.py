from rest_framework import serializers
from django.core.validators import RegexValidator
from computer.models import ComputerModel


class ComputerSerializer(serializers.ModelSerializer):
	CPU = serializers.FloatField(min_value=1.0, max_value=5.5)
	brand = serializers.CharField(validators=[
			RegexValidator('^[a-zA-Z0-9]{2,20}$', 'only alpha min 2ch max 30ch')
	])

	class Meta:
		model = ComputerModel
		fields = '__all__'
