from django.urls import path
from . import views 

urlpatterns = [
    path('',views.activities,name='activities'),
    path('createactivities',views.create_activity,name='create-activity'),
    path('updateactivity/<str:id>',views.update_activity,name='update-activity'),
 ]
