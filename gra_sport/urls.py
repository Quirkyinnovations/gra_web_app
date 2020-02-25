from django.urls from path
from .import views


#namespace
app_name = 'sports'

urlpatterns = [
    path('', views.index, name="index")
]