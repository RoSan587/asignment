from django.forms import ModelForm
from .models import Activity
from officer.models import Officer

class createActivityForm(ModelForm):
	class Meta:
		model = Activity
		exclude = ['is_cancelled']

class updateActivityForm(ModelForm):
	class Meta:
		model = Activity
		exclude = ['is_active','activitytype']


