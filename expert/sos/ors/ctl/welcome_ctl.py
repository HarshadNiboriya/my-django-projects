from django.shortcuts import render

from .base_ctl import BaseCtl
from ..service.user_service import UserService


class WelcomeCtl(BaseCtl):

    def display(self, request,params = {}):
        return render(request, self.get_template())

    def submit(self, request,params = {}):
        return render(request, self.get_template())

    def get_service(self):
            return UserService()

    def get_template(self):
            return 'welcome.html'
