from django.urls import path
from . import views 

urlpatterns = [
    path('',views.officerinfo,name="officerinfo"),
    path('workdays/',views.officerworkdays,name="officerworkdays"),
    path('create-officer/',views.createofficer,name="create-officer"),
    path('addworkdays/',views.addworkdays,name='addworkdays'),
    path('updateworkdays/<str:id>/',views.updateworkdays,name='updateworkdays'),
    path('update-officer/<str:id>/',views.updateofficer,name="update-officer"),
]