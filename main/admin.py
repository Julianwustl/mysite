from django.contrib import admin
from main.models import city, country,department,project
# Register your models here.
admin.site.register(city)
admin.site.register(country)
admin.site.register(department)
admin.site.register(project)
