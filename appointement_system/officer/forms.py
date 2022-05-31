from django import forms
from django.forms import ModelForm
from .models import Officer,Workdays

class OfficerForm(ModelForm):
	"""docstring for OfficerForm"""
	class Meta:
		model = Officer
		exclude = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'post': forms.TextInput(attrs={'class':'form-control'}),
			'workstartTime': forms.TimeInput(attrs={'class':'form-control','placeholder':'12:00:00 am'}),
			'workendTime': forms.TimeInput(attrs={'class':'form-control','placeholder':'12:00:00 am'}),

		}

class Workdaysform(ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Workdays
		fields = '__all__'
		widgets = {
			'officer': forms.Select(attrs={'class':'form-control'}),
			'workday_from':forms.Select(attrs={'class':'form-control'}),
			'workday_to': forms.Select(attrs={'class':'form-control'}),

		}
	
		

		