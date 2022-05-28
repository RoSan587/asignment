from django.forms import ModelForm
from .models import Officer,Workdays

class OfficerForm(ModelForm):
	"""docstring for OfficerForm"""
	class Meta:
		model = Officer
		exclude = '__all__'

class Workdays(ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Workdays
		fields = '__all__'
	
		

		