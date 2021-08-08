from  . import views 
from django.urls import path


urlpatterns = [
    path("vet/", views.VetList, name="home"),
    
] 
