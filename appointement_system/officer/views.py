from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Officer
from .forms import OfficerForm


# My views here.

def officerinfo(request):
	officers = Officer.objects.all()
	print(officers)	
	return render(request,'officer/officerinfo.html',{'content':officers})

def createofficer(request):
	form = OfficerForm()
	content = {'form': form} 	
	if request.method == 'POST' :
		form = OfficerForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('home_page')
	return render(request,'officer/createofficer.html',content)

def updateofficer(request,id):
	officer = Officer.objects.get(id=id)
	form = OfficerForm(instance=officer)
	content = {'form': form} 	
	if request.method == 'POST' :
		form = OfficerForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('home_page')
	return render(request,'officer/createofficer.html',content)