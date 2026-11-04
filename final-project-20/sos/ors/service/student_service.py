from ..dao.student_dao import StudentDAO
from ..service.base_service import BaseService


class StudentService(BaseService):

    def get_dao(self):
        return StudentDAO()