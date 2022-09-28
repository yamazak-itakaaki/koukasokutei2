"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from re import template
from typing import Generic
from django.urls import path

from . import views



app_name = 'blog'
urlpatterns = [

    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inqiry"),
    path('blog-list/', views.BloglistView.as_view(), name="list"),
    path('blog-betail/', views.BlogbetailView.as_view(), name="betail"),
    path('blog-create/', views.BlogcreateView.as_view(), name="create"),
    path('blog-update/', views.BlogupdateView.as_view(), name="update"),
    path('blog-delete/', views.BlogdeleteView.as_view(), name="delete"),

    aaa
]
