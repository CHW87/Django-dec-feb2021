from django.contrib import admin

from .models import ComputerModel

# Register your models here.
# admin.site.register(ComputerModel)


@admin.register(ComputerModel)
class ComputerAdmin(admin.ModelAdmin):
	list_display = ('id', 'brand', 'model', 'RAM')

