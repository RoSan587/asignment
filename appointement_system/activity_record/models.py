from django.db import models
from django.utils import timezone
from officer.models import Officer
from visitors.models import Visitors
# Create your models here.
class Activity(models.Model):
	"""docstring for Activity"""
	officerid = models.ForeignKey(Officer, on_delete= models.SET_NULL,null=True)
	visitorid = models.ForeignKey(Visitors, on_delete=models.SET_NULL,null=True,blank=True)
	TYPE = [('L','Leave'), ('ap','appointmnet'), ('b','break')]
	activitytype =	models.CharField(max_length=50,
		choices=TYPE,
		default='appointmnet'
		)
	is_active = models.BooleanField(default=True)
	date = models.DateField(auto_now=False, auto_now_add=True)
	start_time = models.TimeField(auto_now=False, auto_now_add=False) 
	end_time = models.TimeField(auto_now=False, auto_now_add=False)
	addedd_on = models.DateTimeField(default=timezone.now())
	comment = models.CharField(max_length=50)
	is_cancelled = models.BooleanField(default=False)

	def __str__(self):
		return self.comment
	 
		