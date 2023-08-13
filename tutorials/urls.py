from . import views
from django.urls import path

urlpatterns = [
    path('', views.tutorials_me, name='tutorials'),
]
