from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Visitors
from .forms import VisitorForm
# Create your views here.
def createvisitor(request):
	form = VisitorForm()
	content = {'form':form}
	if request.method == "True":
		form = VisitorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home_page')
		else:
			messages.error(request, 'Please enter valid value')

	return render(request, 'visitors/createvisitor.html',content) 

def visitorinfo(request):
	visitors = Visitors.objects.all()
	return render(request,'visitors/visitorinfo.html',{'content':visitors})

def updatevisitor(request,id):
	visitor = Visitors.objects.get(id=id)
	form = VisitorForm(instance=visitor)
	content = {'form':form}
	if request.method == "POST":
		form = VisitorForm(request.POST,instance=visitor)
		if form.is_valid():
			form.save()
			return redirect('home_page')
		else:
			messages.error(request, 'Please enter valid value')
	return render(request, 'visitors/createvisitor.html',content)

