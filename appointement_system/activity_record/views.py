from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from django.contrib import messages
from .forms import createActivityForm, updateActivityForm
from .models import Activity
from officer.models import Officer, Workdays
from visitors.models import Visitors
from .filters import Activityfilter 
# Create your views here.
def create_activity(request):
	form = createActivityForm()
	content = {'form':form}
	if request.method == "POST":
		visitor_status = True
		officer = request.POST.get('officer')
		officer_status = Officer.objects.values_list('is_active',flat=True).get(id=officer)
		try:
			visitor = request.POST.get('visitor')
			visitor_status = Visitors.objects.values_list('is_active',flat=True).get(id=visitor)
		except:
			pass
		
		if officer_status == True and visitor_status == True:
			form = createActivityForm(request.POST)
			if form.is_valid():
				if activity_datetime_check(request,form):
					form.save()
					return redirect('home_page')
			else:
				messages.error(request,"Enter the valid value")
		else:
			messages.error(request,"Officer or Visitor may be Inactivte")
	return render(request,'activity_record/create_activity.html',content)


def update_activity(request,id):
	activity = Activity.objects.get(activityid=id)
	form = updateActivityForm(instance=activity)
	content = {'form':form}
	if request.method == "POST":
		form = updateActivityForm(request.POST,instance=activity)
		if form.is_valid():
			form.save()
			return redirect('home_page')
		else:
			messages.error(request,"Enter the valid value")
	return render(request,'activity_record/create_activity.html',content)

def activities(request):
	activities = Activity.objects.all()
	content = {'activities':activities}
	form = Activityfilter()
	content = {'form': form}
	myFilter = Activityfilter(request.GET, queryset=activities)
	activities = myFilter.qs
	content['activities'] = activities
	return render(request,'activity_record/activities.html',content)

def activity_datetime_check(request,instance):
	weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
	date = instance.cleaned_data['date']
	day =date.weekday()
	officer = instance.cleaned_data['officer']
	workdays = Workdays.objects.values_list('workdays',flat=True).get(officer=officer)
	if weekDays[day] in list(workdays):
		return True
	else:
		messages.error(request,"User not availabe in that date")	


