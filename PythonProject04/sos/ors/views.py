from django.http import HttpResponse

from django.shortcuts import render

def test_ors(request):
    return HttpResponse('<h1> ors test view function</h1>')

def display(request):
    return HttpResponse('<h1>ors display function</h1>')

def welcome(request):
    return render(request, 'welcome.html')

def user_signup(request):
    # print(request.GET.get('firstName'))
    # print(request.GET.get('lastName'))
    # print(request.GET.get('loginID'))
    # print(request.GET.get('Password'))
    # print(request.GET.get('Address'))
    # print(request.GET.get('DOB'))
    print(request.POST.get('firstName'))
    print(request.POST.get('lastName'))
    print(request.POST.get('loginID'))
    print(request.POST.get('password'))
    print(request.POST.get('DOB'))
    print(request.POST.get('Address'))
    return render(request, 'registration.html')

def user_signin(request):
    print(request.POST.get('firstName'))
    print(request.POST.get('lastName'))
    return render(request, 'login.html')