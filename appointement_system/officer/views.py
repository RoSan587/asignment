from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Officer, Workdays
from .forms import OfficerForm, Workdaysform
from activity_record.models import Activity 


# My views here.

def officerinfo(request):
	officers = Officer.objects.all()
	content = {'officers':officers}
	return render(request,'officer/officerinfo.html',content)

def officerworkdays(request):
	workdays = Workdays.objects.all()
	content = {'workdays':workdays}
	return render(request,'workdays/workdays.html',content)

def createofficer(request):
	form = OfficerForm()
	content = {'form': form} 	
	if request.method == 'POST' :
		form = OfficerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('addworkdays')
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
			return redirect('updateworkdays',id)
	return render(request,'officer/createofficer.html',content)

def addworkdays(request):
	form = Workdaysform()
	content = {'form': form} 	
	if request.method == 'POST' :
		form = Workdaysform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home_page')
		else:
			messages.error(request, 'User Already has the workdays saved')
	return render(request,'officer/workdaysform.html',content)

def updateworkdays(request,id):
	workday = Workdays.objects.get(officer=id)
	form = Workdaysform(instance=workday)
	content = {'form': form} 	
	if request.method == 'POST':
		form = Workdaysform(request.POST,instance=workday)
		if form.is_valid():
			form.save()
			return redirect('home_page')
	return render(request,'officer/workdaysform.html',content)

