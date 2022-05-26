from django.db import models
from officer.models import Officer
# Create your models here.
class Activity(models.Model):
	"""docstring for Activity"""
	officerID = models.ForeignKey(Officer, on_delete= models.SET_NULL,null=True)
	#visitorID = models.ForeignKey(Artist, on_delete=models.NOT_NULL
	Name = models.CharField(max_length=50)
	TYPE = [('Leave','Leave'), ('appointmnet','appointmnet'), ('break','break')]
	Type =	models.CharField(max_length=50,
		choices=TYPE,
		default='appointmnet'
		)
	STATUS = [('active','active'), ('inactive','inactive')]
	Status =	models.CharField(max_length=50,
		choices=STATUS,
		default='active'
		)
	date = models.DateField(auto_now=False, auto_now_add=True)
	start_time = models.TimeField(auto_now=False, auto_now_add=False) 
	end_time = models.TimeField(auto_now=False, auto_now_add=False)
	addedd_on = models.DateTimeField(auto_now=False, auto_now_add=False)
	 
		