from django.shortcuts import render

from .base_ctl import BaseCtl
from ..models import Course
from ..service.course_service import CourseService
from ..utility.data_validator import DataValidator


class CourseCtl(BaseCtl):

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("description", ''))):
            input_error['description'] = 'Description is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("duration", ''))):
            input_error['duration'] = 'Duration is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['name'] = request.POST.get('name')
        self.form['description'] = request.POST.get('description')
        self.form['duration'] = request.POST.get('duration')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.name = self.form['name']
        obj.description = self.form['description']
        obj.duration = self.form['duration']

        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['description'] = obj.description
        self.form['duration'] = obj.duration


    def display(self, request, params={}):
        return render(request, self.get_template(),{'form':self.form})

    def submit(self, request, params={}):

        try:
            course = self.form_to_model(Course())
            self.get_service().save(course)
            if self.form['id'] > 0:
                self.form['message'] = 'Course Updated Successfully...!!!'
                self.form['error'] = False

            else:
                self.form['message'] = 'Course Added Successfully...!!!'
                self.form['error'] = False

        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True

        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return CourseService()

    def get_template(self):
        return 'course.html'


