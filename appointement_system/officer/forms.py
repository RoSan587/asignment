from django.forms import ModelForm
from .models import Officer

class OfficerForm(ModelForm):
	"""docstring for OfficerForm"""
	class Meta:
		model = Officer
		fields = '__all__'

		