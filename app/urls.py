
from django.urls import path

from app import views

urlpatterns = [
    path('', views.home , name='homepage'),
    path('signin', views.signin , name='signin'),
    path('login' , views.user_login , name='loginuser'),
    path('logout', views.user_logout , name='logoutuser'),
    path('contact', views.contact , name='contact'),
    path('enroll', views.enroll, name='enroll'),
    path('profile', views.Profile, name='profile'),
    path('gallary', views.gallary, name='gallary'),
    path('attendence', views.attendence, name='attendence'),
    
]
