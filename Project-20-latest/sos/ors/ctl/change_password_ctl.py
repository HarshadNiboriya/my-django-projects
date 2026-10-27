from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..service.user_service import UserService
from ..utility.data_validator import DataValidator


class ChangePasswordCtl(BaseCtl):

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("oldPassword", ''))):
            input_error['old_password'] = 'Old Password is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("newPassword", ''))):
            input_error['new_password'] = 'New Password is required'
            input_error['error'] = True
        new_password = request.POST.get("newPassword", '')
        confirm_password = request.POST.get("confirmPassword", '')
        if (DataValidator.is_null(request.POST.get("confirmPassword", ''))):
            input_error['confirm_password'] = 'Confirm Password is required'
            input_error['error'] = True

        elif (new_password != confirm_password):
            input_error['confirm_password'] = "New password and Confirm password must be same"
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['old_password'] = request.POST.get('oldPassword')
        self.form['new_password'] = request.POST.get('newPassword')
        self.form['confirm_password'] = request.POST.get('confirmPassword')




    def display(self, request,params = {}):
        return render(request,self.get_template(), {'form': self.form})

    def submit(self, request, params = {}):
        id = request.session['id']
        user = self.get_service().get(id)

        new_password = request.POST.get("newPassword", '')
        confirm_password = request.POST.get("confirmPassword", '')

        if request.POST.get('oldPassword') != user.password:
            self.form['message'] = " old password is incorrect "
            self.form['error'] = True
        else:
            if new_password == confirm_password:
                user.password = new_password
                self.get_service().save(user)
                self.form['message'] = " password changed successfully "

        return render(request,self.get_template(), {'form': self.form})


    def get_service(self):
         return UserService()

    def get_template(self):
            return 'changepassword.html'