from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import createActivityForm, updateActivityForm
from .models import Activity
from officer.models import Officer
from .filters import Activityfilter 
# Create your views here.
def create_activity(request):
	form = createActivityForm()
	content = {'form':form}
	if request.method == "POST":
		officer = request.POST.get('officer')
		if Officer.objects.values_list('is_active',flat=True).get(id=officer):
			form = createActivityForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('home_page')
			else:
				messages.error(request,"Enter the valid value")
		else:
			messages.error(request,"Officer is Inactivte")
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
	content['form'] = form
	myFilter = Activityfilter(request.GET, queryset=activities)
	activities = myFilter.qs
	content['activities'] = activities
	return render(request,'activity_record/activities.html',content)