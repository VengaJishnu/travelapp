from django.contrib import admin
from .models import Place,assignment
# Register your models here.
admin.site.register(Place)   #to show the model in admin panel
admin.site.register(assignment)