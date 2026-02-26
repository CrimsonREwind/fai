from django.shortcuts import render

# Create your views here.

def home(request):
    # Dummy context for testing frontend
    context = {
        'coins': 150,
        'notifications': 3,
    }
    return render(request, 'home.html', context)

def settings_view(request):
    return render(request, 'settings.html')


