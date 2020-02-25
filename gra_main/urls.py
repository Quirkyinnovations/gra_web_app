from django.urls import path
from . import views
# from gra_blog.views import 


name_app = 'app'

urlpatterns =[
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('branches/', views.branches, name='branches'),
    path('mission/', views.mission, name='mission'),
    path('department/', views.department, name='department'),
    path('channel/', views.channel, name='channel'),
    path('contactus/', views.contactus, name='contactus'),
    path('sermons/', views.sermons, name='sermons'),
    path('events/', views.events, name='events'),
    path('shop/', views.shop, name='shop'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('media/', views.media, name='media'),
    path('channel/', views.channel, name='channel'),
    path('music/', views.music, name='music'),
    path('addUser/', views.addUser, name='addUser'),
    path('addModelForm/', views.addModelForm, name='addModelForm'),
    path('modelForm/', views.modelForm, name='modelForm'),
]