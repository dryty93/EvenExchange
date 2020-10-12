from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views
from .models import Profile

urlpatterns = [
    path('',views.index, name='index'),
    #path('<slug:slug>',views.prof, name='prof'),
  #  path('Profile/', views.prof, name='prof'),
   # path('<slug:slug>',views.prof, name='profile'),
    url(r'^Profile/', views.prof, name='profile'),

    path('editProf', views.editProf, name='edit_prof'),

]