from django.shortcuts import render

from .base_ctl import BaseCtl
from ..service.marksheet_service import MarksheetService


class MarksheetListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['name'] = request.POST.get('name')

    def display(self, request,params = {}):
        marksheet_list = self.get_service().search(self.form)
        self.form['list'] = marksheet_list
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

        marksheet_list = self.get_service().search(self.form)
        self.form['list'] = marksheet_list

        return render(request, self.get_template(), {"form": self.form})

    def get_service(self):
        return MarksheetService()

    def get_template(self):
        return 'marksheetlist.html'