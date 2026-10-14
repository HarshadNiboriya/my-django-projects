from django.shortcuts import render

from sos.ors.ctl.base_ctl import BaseCtl
from sos.ors.service.role_service import RoleService
from sos.ors.service.test_html_utility import role_list
from sos.ors.service.user_service import UserService
from sos.ors.utility.html_utility import HtmlUtility


class TestCtl(BaseCtl):
    def request_to_form(self,request):
    self.['role_id'] = request.POST.get('roleId')
    self.form['gender'] = request.POST.get('gender')
    self.form['user_id'] = request.POST.get('userId','')


    def preload(self, request):
        gender_list = ["Male", "Female"]
        role_list = RoleService.search({})
        user_list = UserService().search({})

        self.preload_data["gender_select"] = HtmlUtility.get_list_from_list(
            "gender",
            self.form.get("gender"),
            gender_list
        )

        self.preload_data['role_select'] = HtmlUtility.get_list_from_beans(
            "roleId",
            int(self.form.get("role_id") or 0),
            role_list
        )
        self.preload_data["user_select"] = HtmlUtility.get_list_from_beans(
            "userId",
            int(self.form.get("id") or 0),
            user_list
        )

        def display(self, request, params={}):
            return render(request,'test.html', {'form': self.form,"preload_data":self.preload(request)})

        def submit(self, request, params={}):
            if request.POST.get('operation','') == 'signin':
                return render(request,'test.html',{'form':self.form,"preload_data":self.preload(request)})