from django.db.models.expressions import result
from django.shortcuts import render
from pyexpat.errors import messages

from .service.UserService import UserService


def welcome(request):
    return render(request, 'welcome.html')


def sign_up(request):
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
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        service = UserService()
        service.add(form)

    return render(request, 'registration.html')


def sign_in(request):
    # print(request.POST.get('loginID'))
    # print(request.POST.get('Password'))
        message = ''
        if request.method == "POST":
            form = {}
            form['login_id'] = request.POST.get('loginId')
            form['password'] = request.POST.get('password')

            service = UserService()
            records = service.authenticate(form['login_id'], form['password'])

            if len(records) > 0:
                return render(request, 'welcome.html', {'firstName': records[0].get('first_name')})
            else:
                message = 'login & password invalid'

        return render(request, 'login.html', {'message': message})