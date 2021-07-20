from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class CarModel(models.Model):
	class Meta:
		db_table = 'cars'
		app_label = 'core'

	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	year = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
