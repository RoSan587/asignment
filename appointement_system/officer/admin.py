from django.contrib import admin

# Register your models here 
from officer.models import Officer,workdays
admin.site.register(Officer)
admin.site.register(workdays)