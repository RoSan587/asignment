from django.db import models

# Create your models here.
class Officer(models.Model):
	"""docstring for Officer"""
	Name =	models.CharField(max_length=50)
	Post =	models.CharField(max_length=50)
	STATUS = [('A','active'), ('I','inactive')]
	Status =	models.CharField(max_length=50,
		choices=STATUS,
		default='active'
		)
	WorkstartTime =	models.TimeField()
	WorkendTime =	models.TimeField()

	def __str__(self):
		return self.Name

class workdays(models.Model):
	"""docstring for workdays"""
	OfficerID = models.ForeignKey(Officer,on_delete=models.SET_NULL,null=True)
	workdays  = models.CharField(max_length=50)


