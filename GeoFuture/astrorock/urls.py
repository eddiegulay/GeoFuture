from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_view, name='init_view'),
    path('interactive-map/', views.interactive_maps_view, name='interactive_maps_view'),
    path('geological-analysis/', views.analysis_view, name='analysis_view'),
    path('data-visualization/', views.visualization_view, name='visualization_view'),
    path('rock-detection/', views.rock_detection_view, name='rock_detection_view')
]
