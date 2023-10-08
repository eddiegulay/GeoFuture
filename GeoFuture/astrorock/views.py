from django.shortcuts import render
import os

# Create your views here.
def init_view(request):
    return render(request, "index.html")


def interactive_maps_view(request):
    return render(request, "pages/interactive_map.html")

def analysis_view(request):
    return rock_detection_view(request)

def visualization_view(request):
    return render(request, "pages/data_visualization.html")


def rock_detection_view(request):
    return render(request, "pages/rock_detection.html")


def rock_classification_view(request):
    return render(request, "pages/rock_classification.html")



def rock_spectral_analysis(img):
    """
    This function is used to perform spectral analysis of the rock image.
    
    returns rock_type and percentage of rock_type in the image.
    """

    return 0,0