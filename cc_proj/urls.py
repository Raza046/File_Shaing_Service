"""cc_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login',views.Login, name='login'),
    path('register <str:pk>',views.Register, name='register'),
    path('home',views.Home, name='home'),
    path('logout',views.Logout, name='logout'),
    path('AllPost',views.AllPost, name='AllPost'),
    path('createPost',views.createPost, name='createPost'),
    path('AllUsers',views.AllUsers, name='AllUsers'),
    path('select_register',views.select_register, name='select_register'),
    path('DelPost <str:pk>',views.DelPost, name='DelPost'),

]
