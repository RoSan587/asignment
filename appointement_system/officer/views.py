from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Officer
from .forms import OfficerForm, Workdays
from activity_record.models import Activity 


# My views here.

def officerinfo(request):
	officers = Officer.objects.all()
	return render(request,'officer/officerinfo.html',{'content':officers})

def createofficer(request):
	form = OfficerForm()
	content = {'form': form} 	
	if request.method == 'POST' :
		form = OfficerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home_page')
		else:
			messages.error(request, 'Please enter valid value')
	return render(request,'officer/createofficer.html',content)

def updateofficer(request,id):
	officer = Officer.objects.get(id=id)
	form = OfficerForm(instance=officer)
	content = {'form': form} 	
	if request.method == 'POST':
		form = OfficerForm(request.POST,instance=officer)
		if form.is_valid():
			form.save()
			return redirect('home_page')
	return render(request,'officer/createofficer.html',content)