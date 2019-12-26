"""mysite URL Configuration

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
from cafe import views as cafe_views

urlpatterns = [
    path('', cafe_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', cafe_views.contact, name='contact'),
    path('menu/', cafe_views.menu, name='menu'),
    path('about/', cafe_views.about, name='about'),
    path('reservation/', cafe_views.reservation, name='reservation'),
    path('blog/', cafe_views.blog, name='blog'),
    path('blogsingle/', cafe_views.blogsingle, name='blogsingle'),
]
