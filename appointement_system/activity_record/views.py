from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import createActivityForm, updateActivityForm
from .models import Activity
# Create your views here.
def create_activity(request):
	form = createActivityForm()
	content = {'form':form}
	if request.method == "POST":
		form = createActivityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home.html')
		else:
			messages.error(request,"Enter the valid value")
	return render(request,'activity_record/create_activity.html',content)

def activities(request):
	activities = Activity.objects.all()
	content = {'activities':activities}
	return render(request,'activity_record/activities.html',content)