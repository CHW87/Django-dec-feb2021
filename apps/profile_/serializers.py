from rest_framework import serializers

from core.models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProfileModel
		fields = ('id', 'name', 'age', 'born')
