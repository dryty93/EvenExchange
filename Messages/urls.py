from django.urls import include, path
from . import views


urlpatterns = [
    path('/send',views.sendMessage),
    path('/inbox',views.view_inbox),
     ]