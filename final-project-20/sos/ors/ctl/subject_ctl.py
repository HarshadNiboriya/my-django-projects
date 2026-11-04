from django.shortcuts import render

from .base_ctl import BaseCtl
from ..models import Subject
from ..service.course_service import CourseService
from ..service.subject_service import SubjectService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class SubjectCtl(BaseCtl):

    def preload(self, request):
        course_list = CourseService().search({})
        self.form['preload_list'] = course_list


        self.preload_data["course_select"] = HtmlUtility.get_list_from_beans(
            "courseId",
            self.form.get("course_id"),
            course_list
        )

        return self.preload_data

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("description", ''))):
            input_error['description'] = 'Description is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['course_id']) or request.POST.get("courseId") == "0"):
            input_error['course_id'] = 'course is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['name'] = request.POST.get('name','')
        self.form['description'] = request.POST.get('description','')
        self.form['course_id'] = int(request.POST.get('courseId', 0))

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.name = self.form['name']
        obj.description = self.form['description']
        obj.course_id = int(self.form['course_id'])
        obj.course_name = CourseService().get(self.form['course_id']).name
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['description'] = obj.description
        self.form['course_id'] = obj.course_id
        self.form['course_name'] = obj.course_name


    def display(self, request, params={}):
        return render(request, self.get_template(),{'form': self.form, "preload_data": self.preload(request)})

    def submit(self, request, params={}):

        try:
            subject = self.form_to_model(Subject())
            self.get_service().save(subject)
            if self.form['id'] > 0:
                self.form['message'] = 'Subject Updated Successfully...!!!'
                self.form['error'] = False

            else:
                self.form['message'] = 'Subject Added Successfully...!!!'
                self.form['error'] = False

        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True

        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def get_service(self):
        return SubjectService()

    def get_template(self):
        return 'subject.html'


