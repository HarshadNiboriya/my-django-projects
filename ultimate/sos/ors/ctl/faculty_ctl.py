from django.shortcuts import render

from .base_ctl import BaseCtl
from ..models import Faculty, College, Subject, Course
from ..service.college_service import CollegeService
from ..service.course_service import CourseService
from ..service.faculty_service import FacultyService
from ..service.subject_service import SubjectService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class FacultyCtl(BaseCtl):

    def preload(self, request):
        gender_list = ["Male", "Female"]

        college_list = CollegeService().search({})
        self.form['preload_list'] = college_list

        subject_list = SubjectService().search({})
        self.form['preload_list'] = subject_list

        course_list = CourseService().search({})
        self.form['preload_list'] = course_list

        self.preload_data["gender_select"] = HtmlUtility.get_list_from_list(
            "gender",
            self.form.get("gender"),
            gender_list
        )
        self.preload_data["college_select"] = HtmlUtility.get_list_from_beans(
            "collegeId",
            self.form.get("college_id"),
            college_list
        )
        self.preload_data["subject_select"] = HtmlUtility.get_list_from_beans(
            "subjectId",
            self.form.get("subject_id"),
            subject_list
        )
        self.preload_data["course_select"] = HtmlUtility.get_list_from_beans(
            "courseId",
            self.form.get("course_id"),
            course_list
        )
        return self.preload_data

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['first_name'] = request.POST.get('firstName','')
        self.form['last_name'] = request.POST.get('lastName','')
        self.form['email'] = request.POST.get('email','')
        self.form['password'] = request.POST.get('password','')
        self.form['address'] = request.POST.get('address','')
        self.form['gender'] = request.POST.get('gender','')
        self.form['dob'] = request.POST.get('dob','')
        self.form['college_id'] = int(request.POST.get('collegeId', 0))
        self.form['subject_id'] = int(request.POST.get('subjectId', 0))
        self.form['course_id'] = int(request.POST.get('courseId', 0))


    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.first_name = self.form['first_name']
        obj.last_name = self.form['last_name']
        obj.email = self.form['email']
        obj.password = self.form['password']
        obj.address = self.form['address']
        obj.gender = self.form['gender']
        obj.dob = self.form['dob']
        obj.college_id = int(self.form['college_id'])
        obj.college_name = CollegeService().get(self.form['college_id']).name
        obj.subject_id = int(self.form['subject_id'])
        obj.subject_name = SubjectService().get(self.form['subject_id']).name
        obj.course_id = int(self.form['course_id'])
        obj.course_name = CourseService().get(self.form['course_id']).name
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['first_name'] = obj.first_name
        self.form['last_name'] = obj.last_name
        self.form['email'] = obj.email
        self.form['password'] = obj.password
        self.form['address'] = obj.address
        self.form['gender'] = obj.gender
        self.form['dob'] = obj.dob.strftime('%Y-%m-%d')
        self.form['college_id'] = obj.college_id
        self.form['college_name'] = obj.college_name
        self.form['subject_id'] = obj.subject_id
        self.form['subject_name'] = obj.subject_name
        self.form['course_id'] = obj.course_id
        self.form['course_name'] = obj.course_name

    def input_validation(self, request):
        input_error = self.form['input_error']
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("firstName", ''))):
            input_error['first_name'] = 'First Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("lastName", ''))):
            input_error['last_name'] = 'Last Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("email", ''))):
            input_error['email'] = 'email is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("password", ''))):
            input_error['password'] = 'Password is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("address", ''))):
            input_error['address'] = 'address is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['gender']) or request.POST.get("gender") == "0"):
            input_error['gender'] = 'Gender is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("dob", ''))):
            input_error['dob'] = 'DOB is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['college_id']) or request.POST.get("collegeId") == "0"):
            input_error['college_id'] = 'college is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['subject_id']) or request.POST.get("subjectId") == "0"):
            input_error['subject_id'] = 'subject is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['course_id']) or request.POST.get("courseId") == "0"):
            input_error['course_id'] = 'course is required'
            input_error['error'] = True

        return input_error['error']

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def submit(self, request, params={}):

        try:
            faculty = self.form_to_model(Faculty())
            self.get_service().save(faculty)
            if self.form['id'] > 0:
                self.form['message'] = 'faculty Updated Successfully...!!!'
                self.form['error'] = False
            else:
                self.form['message'] = 'faculty Added Successfully...!!!'
                self.form['error'] = False

        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True

        return render(request, self.get_template(), {'form': self.form, "preload_data": self.preload(request)})

    def get_service(self):
        return FacultyService()

    def get_template(self):
        return 'faculty.html'