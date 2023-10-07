from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_view, name='init_view')
]
