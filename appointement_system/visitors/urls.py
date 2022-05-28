from django.urls import path
from . import views 

urlpatterns = [
    path('',views.visitorinfo,name="visitorinfo"),
    path('create-visitor',views.createvisitor,name="create-visitor"),
    path('update-visitor/<str:id>/',views.updatevisitor,name="update-visitor"),
]