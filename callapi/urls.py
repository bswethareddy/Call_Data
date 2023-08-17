# call_records/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('initiate-call/', views.initiate_call, name='initiate-call'),
    path('call-report/', views.call_report, name='call-report'),
    path('', views.home_page, name='home-page'),
]
