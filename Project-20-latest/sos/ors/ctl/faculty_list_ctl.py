

from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..service.faculty_service import FacultyService


class FacultyListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['first_name'] = request.POST.get('firstName')

    def display(self, request, params={}):
        faculty_list = self.get_service().search(self.form)
        self.form['list'] = faculty_list
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request,params = {}):

        if request.POST['operation'] == "next":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] += 1

        if request.POST['operation'] == "previous":
            self.form['page_no'] = int(request.POST.get('pageNo'))
            self.form['page_no'] -= 1

        if request.POST['operation'] == "search":
            self.form['page_no'] = 1
            self.request_to_form(request)

        self.form['list'] = self.get_service().search(self.form)
        return render(request, self.get_template(), {"form": self.form})

    def get_service(self):
        return FacultyService()

    def get_template(self):
        return 'facultylist.html'