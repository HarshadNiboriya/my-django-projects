from django.shortcuts import render

from ..ctl.base_ctl import BaseCtl


class WelcomeCtl(BaseCtl):

    def display(self, request,params = {}):
        return render(request, 'welcome.html')

    def submit(self, request,params = {}):
        return render(request, 'welcome.html')