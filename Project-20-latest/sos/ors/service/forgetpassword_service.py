from .base_service import BaseService
from ..dao.user_dao import UserDAO
from ..models import User


class ForgetPasswordService(BaseService):

    def get_dao(self):
        return UserDAO()

    def forget_password(self, login_id):
        objs = self.get_dao().find_by_unique_key('login_id', login_id)

        if objs.exists():
            return objs.first()
        else:
            raise Exception('Login Id Incorrect')

    def get(self):
        return User