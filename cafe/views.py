from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'cafe/home.html', {})  
def about(request):
    return render(request, 'cafe/about.html', {})  
def blog(request):
    return render(request, 'cafe/blog.html', {})  
def blogsingle(request):
    return render(request, 'cafe/blogsingle.html', {}) 
def contact(request):
    return render(request, 'cafe/contact.html', {})  
def menu(request):
    return render(request, 'cafe/menu.html', {})  
def reservation(request):
    return render(request, 'cafe/reservation.html', {})  

# Create your views here.
