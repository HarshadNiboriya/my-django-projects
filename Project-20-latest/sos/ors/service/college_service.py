from ..dao.college_dao import CollegeDAO
from ..service.base_service import BaseService


class CollegeService(BaseService):

    def get_dao(self):
        return CollegeDAO()