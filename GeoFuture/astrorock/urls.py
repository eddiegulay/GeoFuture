from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_view, name='init_view'),
    path('interactive-map/', views.interactive_maps_view, name='interactive_maps_view'),
]
