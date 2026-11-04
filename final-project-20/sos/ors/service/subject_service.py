from ..dao.subject_dao import SubjectDAO
from ..service.base_service import BaseService


class SubjectService(BaseService):

    def get_dao(self):
        return SubjectDAO()