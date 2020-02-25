from django.urls import path
from .import views


#namespace
app_name = 'news'

urlpatterns = [
    path('', views.index, name="index")
]
