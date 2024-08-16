from django.contrib import admin
from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('index/',views.index,name='index'),
    path('listtopics/', views.listing_topics,name='topics'),
    path('loginform/',views.login_check,name='loginform'),
    path('users/',views.usersform,name='user'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name="logout"),
    path('specical/',views.special,name='special'),
    path('login/',views.user_login,name='user_login'),
]

