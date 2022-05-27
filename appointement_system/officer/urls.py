from django.urls import path
from . import views 

urlpatterns = [
    path('',views.officerinfo,name="officerinfo"),
    path('create-officer',views.createofficer,name="create-officer"),
    path('update-officer/<str:id>/',views.updateofficer,name="update-officer"),
]