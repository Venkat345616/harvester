"""
URL configuration for harvesterproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from harvesterapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('farmer',views.farmer,name="farmer"),
    path('login',views.login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('owner_details/<str:owner_name>/', views.owner_details, name='owner_details'),
    path('search/', views.search_farmers, name='search_farmers'),
    path('farmer/<str:farmer_name>/', views.farmer_details, name='farmer_details'),
    
   
]
