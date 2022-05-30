import django_filters
from django_filters import FilterSet,DateFilter,TimeFilter
from .models import Activity


class Activityfilter(FilterSet):
 	"""docstring for activityfilter"""
 	start_date = DateFilter(field_name="addedd_on", lookup_expr='gte')
 	end_date = DateFilter(field_name="addedd_on", lookup_expr='lte')
 	class Meta:
 		model = Activity
 		fields = ['is_active','activitytype','officer', 'visitor','is_cancelled']
 			


