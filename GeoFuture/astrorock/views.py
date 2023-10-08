from django.shortcuts import render

# Create your views here.
def init_view(request):
    return render(request, "index.html")


def interactive_maps_view(request):
    return render(request, "pages/interactive_map.html")

def analysis_view(request):
    return render(request, "pages/analytic_tools.html")

def visualization_view(request):
    return render(request, "pages/data_visualization.html")