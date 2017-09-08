from django.conf.urls import url
from orderManager import views

urlpatterns = [
    url(r'^order/$', views.create_order)
]