from django.shortcuts import render
from django.http import HttpResponse
from .models import Officer
# Create your views here.
def officerinfo(request):
	officers = Officer.objects.all()	
	return render(request,'officer/officerinfo.html',{'content':officers})