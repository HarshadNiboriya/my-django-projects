from sqlite3.dbapi2 import paramstyle

from .base_service import BaseService
from ..dao.user_dao import UserDAO
from ..mail.email_builder import EmailBuilder
from ..mail.email_details import EmailDetails
from ..mail.email_service import EmailService
from ..models import User


class UserService(BaseService):

    def get_dao(self):
        return UserDAO()

    def authenticate(self, login_id, password):

        users = self.get_dao().find_by_unique_key('login_id', login_id)

        if users.exists():
            user = users.first()
            if user.password == password:
                return user
            else:
                return None
        else:
            return None

    def user_register(self, obj):
        self.save(obj)

        details = EmailDetails()
        details.to = [obj.login_id]
        details.subject = 'User Registration Successfully'
        details.text = EmailBuilder.sign_up(obj)


        EmailService.send(details)

    def user_change_password(self,obj):
        self.save(obj)

        details = EmailDetails()
        details.to = [obj.login_id]
        details.subject = "Password Changed Successfully"

        params = {
            'firstName': obj.first_name,
            'lastName' : obj.last_name,
            'loginId' : obj.login_id,
            'password' : obj.password
        }
        details.txt = EmailBuilder.change_password(params)

        EmailService.send(details)



    def forget_password(self, login_id):

        users = self.get_dao().find_by_unique_key('login_id', login_id)

        if users.exists():

            user = users.first()

            details = EmailDetails()
            details.to = [user.login_id]
            details.subject = 'Forgot Password - ORS'

            params = {
                'firstName': user.first_name,
                'lastName': user.last_name,
                'loginId': user.login_id,
                'password': user.password
            }

            details.text = EmailBuilder.forgot_password(params)

            EmailService.send(details)

        else:
            raise Exception('Login Id Incorrect')