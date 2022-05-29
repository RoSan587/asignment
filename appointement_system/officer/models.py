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
	"""docstring for workdays"""
	officer = models.ForeignKey(Officer,on_delete=models.SET_NULL,null=True)
	workdays  = models.CharField(max_length=50)


