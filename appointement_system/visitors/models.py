from django.db import models

# Create your models here.
class Visitors(models.Model):
	"""docstring for Visitors"""
	Name = models.CharField(max_length=50)
	mbl_no = models.DecimalField(max_digits=10, decimal_places=0)
	email = models.EmailField(max_length=50)
	STATUS = [('A','active'), ('I','inactive')]
	Status =	models.CharField(max_length=50,
		choices=STATUS,
		default='active'
		)

	def __str__(self):
		return self.Name

