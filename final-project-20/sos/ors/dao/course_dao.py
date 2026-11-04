from .base_dao import BaseDAO
from ..models import Course
from ..utility.data_validator import DataValidator

class CourseDAO(BaseDAO):

    def get_unique_key(self):
        return "name"

    def get_model(self):
        return Course

    def get_label(self):
        return "Course Name"

    def get_where_clause(self, query, params):
        value = params.get("name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(name__istartswith=value.strip())

        return query