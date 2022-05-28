from django.forms import ModelForm
from .models import Activity

class createActivityForm(ModelForm):
	class Meta:
		model = Activity
		exclude = ['is_cancelled']

class updateActivityForm(ModelForm):
	class Meta:
		model = Activity
		fields = '__all__'

