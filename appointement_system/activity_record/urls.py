from django.urls import path
from . import views 

urlpatterns = [
    path('k',views.activities,name='activities'),
    path('',views.create_activity,name='create-activity'),
    path('activities/',views.activities,name='update-activity'),
 ]
