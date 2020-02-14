from django.shortcuts import render

# widok do wyswietlania strony glownej 127.0.0.1:8000
def homepage(request):
    return render(request, 'homepage/homepage.html')