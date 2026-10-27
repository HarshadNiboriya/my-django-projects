from ..dao.course_dao import CourseDAO
from ..service.base_service import BaseService


class CourseService(BaseService):

    def get_dao(self):
        return CourseDAO()