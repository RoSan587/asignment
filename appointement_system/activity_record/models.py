from django.db import models
from django.utils import timezone
from officer.models import Officer
from visitors.models import Visitors
from django.db.models.signals import post_save,pre_save
# Create your models here.
class Activity(models.Model):
	"""docstring for Activity"""
	activityid = models.AutoField(primary_key=True)
	officer = models.ForeignKey(Officer, on_delete= models.SET_NULL,null=True)
	visitor = models.ForeignKey(Visitors, on_delete=models.SET_NULL,null=True,blank=True)
	TYPE = [('Leave','Leave'), ('Appointment','Appointment'), ('Break','Break')]
	activitytype =	models.CharField(max_length=50,
		choices=TYPE,
		default='Appointment'
		)
	is_active = models.BooleanField(default=True)
	date = models.DateField(auto_now=False, auto_now_add=False)
	start_time = models.TimeField(auto_now=False, auto_now_add=False) 
	end_time = models.TimeField(auto_now=False, auto_now_add=False)
	addedd_on = models.DateTimeField(default=timezone.now())
	comment = models.CharField(max_length=50)
	is_cancelled = models.BooleanField(default=False)


	def __str__(self):
		return self.comment


def activity_status_check(sender,instance,created,**kargs):
	if created == False:
		activities = Activity.objects.all()
		for activity in activities:
			officer_status = True
			visitor_status = True
			try:
				officer_status = Officer.objects.values_list('is_active',flat=True).get(id=activity.officer.id)
				visitor_status = Visitors.objects.values_list('is_active',flat=True).get(id=activity.visitor.id)
			except:
				pass
			if officer_status and visitor_status:
				activity.is_active = True
				activity.save()
			else:
				activity.is_active = False
				activity.save()


post_save.connect(activity_status_check,sender=Officer)
post_save.connect(activity_status_check,sender=Visitors)
				