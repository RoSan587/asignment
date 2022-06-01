from django import forms
from django.forms import ModelForm
from .models import Activity
from officer.models import Officer
from visitors.models import Visitors

class createActivityForm(ModelForm):
	class Meta:
		model = Activity
		exclude = ['is_cancelled']
		widgets = {
			'officer':forms.Select(attrs={'class':'form-control'}),
			'visitor':forms.Select(attrs={'class':'form-control'}),
			'activitytype':forms.Select(attrs={'class':'form-control'}),
			'date':forms.SelectDateWidget(attrs={'class':'form-control'}),
			'start_time':forms.TimeInput(attrs={'class':'form-control','placeholder':'12:00:00(use 24 hrs format)'}),
			'end_time':forms.TimeInput(attrs={'class':'form-control','placeholder':'12:00:00(use 24 hrs format)'}),
			'addedd_on':forms.DateTimeInput(attrs={'class':'form-control'}),
			'comment':forms.TextInput(attrs={'class':'form-control'}),
		}
	




class updateActivityForm(ModelForm):
	class Meta:
		model = Activity
		exclude = ['is_active','activitytype']
		widgets = {
			'officer':forms.Select(attrs={'class':'form-control'}),
			'visitor':forms.Select(attrs={'class':'form-control'}),
			'date':forms.SelectDateWidget(attrs={'class':'form-control'}),
			'start_time':forms.TimeInput(attrs={'class':'form-control','placeholder':'12:00:00 am'}),
			'end_time':forms.TimeInput(attrs={'class':'form-control','placeholder':'12:00:00 am'}),
			'addedd_on':forms.DateTimeInput(attrs={'class':'form-control'}),
			'comment':forms.TextInput(attrs={'class':'form-control'}),
		}

