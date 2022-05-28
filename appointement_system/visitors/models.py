from django.db import models

# Create your models here.
class Visitors(models.Model):
	"""docstring for Visitors"""
	name = models.CharField(max_length=50)
	mbl_no = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

 