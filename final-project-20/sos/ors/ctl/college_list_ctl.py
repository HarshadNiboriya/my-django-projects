from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..service.college_service import CollegeService


class CollegeListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['name'] = request.POST.get('name')

    def display(self, request,params = {}):
        college_list = self.get_service().search(self.form)
        self.form['list'] = college_list
        return render(request, self.get_template(), {"form": self.form})

    def submit(self, request,params = {}):

        if request.POST.get('operation', '') == "next":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] += 1
        if request.POST.get('operation', '') == "previous":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] -= 1
        if request.POST.get('operation', '') == "search":
            self.form['page_no'] = 1

        college_list = self.get_service().search(self.form)
        self.form['list'] = college_list

        return render(request, self.get_template(), {"form": self.form})

    def get_service(self):
        return CollegeService()

    def get_template(self):
        return 'collegelist.html'