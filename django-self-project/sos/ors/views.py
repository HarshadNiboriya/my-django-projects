from django.shortcuts import render

from .service.Userservice import UserService

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def signin(request):
    print(request.POST.get('loginID'))
    print(request.POST.get('Password'))
    return render(request, 'login.html')

def signup(request):
    # print(request.GET.get('firstName'))
    # print(request.GET.get('lastName'))
    # print(request.GET.get('loginID'))
    # print(request.GET.get('Password'))
    # print(request.GET.get('Address'))
    # print(request.GET.get('DOB'))

    # print(request.POST.get('firstName'))
    # print(request.POST.get('lastName'))
    # print(request.POST.get('loginID'))
    # print(request.POST.get('Password'))
    # print(request.POST.get('Address'))
    # print(request.POST.get('DOB'))

    if request.method == "POST":
        form = {}
        form['firstname'] = request.POST.get('firstName')
        form['lastname'] = request.POST.get('lastName')
        form['loginid'] = request.POST.get('loginID')
        form['password'] = request.POST.get('Password')
        form['dob'] = request.POST.get('DOB')
        form['address'] = request.POST.get('Address')

        service = UserService()
        service.add(form)

    return render(request,'registration.html')