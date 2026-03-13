from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    context = {
        "title": "Home Title",
        "body": "Home Page"
    }
    return render(request, 'home.html', context)

# home()


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')
