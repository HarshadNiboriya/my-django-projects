from django.shortcuts import render

def welcome(request):
    return render (request,'welcome.html')


def signin(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'registration.html')
