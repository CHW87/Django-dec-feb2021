from django.db import models


# Create your models here.


class ComputerModel(models.Model):
	class Meta:
		db_table = 'computers'
		verbose_name = 'computer'

	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	RAM = models.IntegerField()
	CPU = models.FloatField()
	display = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
