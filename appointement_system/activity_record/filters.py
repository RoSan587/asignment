import django_filters
from django_filters import FilterSet,DateFilter,TimeFilter
from .models import Activity
from django import forms


class Activityfilter(FilterSet):
 	"""docstring for activityfilter"""
 	start_date = DateFilter(
 		widget=forms.SelectDateWidget(attrs={'class':'form-control'}),
 		field_name="date", lookup_expr='gte')
 	end_date = DateFilter(
 		widget=forms.SelectDateWidget(attrs={'class':'form-control'}),
 		field_name="date", lookup_expr='lte')
 	class Meta:
 		model = Activity
 		fields = ['is_active','activitytype','officer', 'visitor','is_cancelled']
 		
 		widgets = {
 		 	'officer':forms.Select(attrs={'class':'form-control'}),
 		 	'visitor':forms.Select(attrs={'class':'form-control'}),
 		 	'activitytype':forms.Select(attrs={'class':'form-control'}),
 		 	'is_cancelled':forms.Select(attrs={'class':'form-control'}),
 		 	}
 		 

