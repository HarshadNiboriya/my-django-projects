from django.http import request
from django.shortcuts import render

from .base_ctl import BaseCtl
from ..models import College
from ..service.college_service import CollegeService
from ..utility.data_validator import DataValidator


class CollegeCtl(BaseCtl):

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("address", ''))):
            input_error['address'] = 'Address is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("state", ''))):
            input_error['state'] = 'State is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("city", ''))):
            input_error['city'] = 'City is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("phone_number", ''))):
            input_error['phone_number'] = 'Phone number is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['name'] = request.POST.get('name')
        self.form['address'] = request.POST.get('address')
        self.form['city'] = request.POST.get('city')
        self.form['state'] = request.POST.get('state')
        self.form['phone_number'] = request.POST.get('phone_number')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.name = self.form['name']
        obj.address = self.form['address']
        obj.city = self.form['city']
        obj.state = self.form['state']
        obj.phone_number = self.form['phone_number']
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['address'] = obj.address
        self.form['city'] = obj.city
        self.form['state'] = obj.state
        self.form['phone_number'] = obj.phone_number

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):

        try:
            college = self.form_to_model(College())
            self.get_service().save(college)
            if self.form['id'] > 0:
                self.form['message'] = 'College Updated Successfully...!!!'
                self.form['error'] = False
            else:
                self.form['message'] = 'College Added Successfully...!!!'
                self.form['error'] = False

        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True

        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return CollegeService()

    def get_template(self):
        return 'college.html'
