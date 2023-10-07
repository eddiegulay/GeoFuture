from django.shortcuts import render

# Create your views here.
def init_view(request):
    return render(request, "index.html")


def interactive_maps_view(request):
    return render(request, "pages/interactive_map.html")