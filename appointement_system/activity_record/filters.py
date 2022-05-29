import django_filters
from django_filters import FilterSet
from .models import Activity


class Activityfilter(FilterSet):
 	"""docstring for activityfilter"""
 	class Meta:
 		model = Activity
 		fields = ['is_active','activitytype','officer', 'visitor','is_cancelled']
 			


