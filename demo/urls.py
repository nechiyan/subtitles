from django.urls import path
from demo import views

urlpatterns = [
    path('', views.home, name='home'),
]