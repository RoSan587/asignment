from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class Officer(models.Model):
	"""docstring for Officer"""
	name =	models.CharField(max_length=50)
	post =	models.CharField(max_length=50)
	is_active =	models.BooleanField(default=True)
	workstartTime =	models.TimeField()
	workendTime =	models.TimeField()

	def __str__(self):
		return self.name

class Workdays(models.Model):
	"""docstring for Workdays"""
	officer = models.OneToOneField(Officer, on_delete= models.SET_NULL,null=True)
	choices = [
		('Sunday','Sunday'),('Mondays','Mondays'),('Tuesday','Tuesday'),
		('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),
		('Saturday','Saturday'),
		]
	workdays = MultiSelectField(max_length=100,choices=choices)

	def  __str__(self):
		return str(self.officer)
 		
