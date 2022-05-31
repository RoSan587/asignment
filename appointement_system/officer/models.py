from django.db import models

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
	officer = models.ForeignKey(Officer, on_delete= models.SET_NULL,null=True)
	choices = [
		(1,'Sunday'),(2,'Mondays'),(3,'Tuesday'),
		(4,'Wednesday'),(5,'Thursday'),(6,'Friday'),
		(7,'Saturday'),
	]
	workday_from = models.DecimalField(max_digits=10,decimal_places=0,choices=choices,default=5)
	workday_to = models.DecimalField(max_digits=10,decimal_places=0,choices=choices,default=4)

	def  __str__():
		return self.officer
 		
