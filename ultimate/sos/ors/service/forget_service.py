
from ..models import User


class ForgetPasswordService:

    def find_by_login(self, login_id):
        print('forget password service orm find_by_login()')
        obj = User.objects.filter(login_id=login_id).first()
        return obj

    def get_model(self):
        return User