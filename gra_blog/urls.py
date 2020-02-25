from django.urls import path
from . import views

# namespace
app_name = 'blog'

urlpatterns = [
    # ex /blog/
    path('', views.index, name='index')
]