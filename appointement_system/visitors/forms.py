from django import forms
from django.forms import ModelForm
from .models import Visitors

class VisitorForm(ModelForm):
	"""docstring for OfficerForm"""
	class Meta:
		model = Visitors
		fields = '__all__'
		widgets = {
			'officer':forms.Select(attrs={'class':'form-control'}),
			'mbl_no': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),

		}
