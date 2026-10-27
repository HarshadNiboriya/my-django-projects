from ..dao.faculty_dao import FacultyDAO
from ..service.base_service import BaseService


class FacultyService(BaseService):

    def get_dao(self):
        return FacultyDAO()