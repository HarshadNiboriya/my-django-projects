from .base_dao import BaseDAO
from ..models import Faculty
from ..utility.data_validator import DataValidator


class FacultyDAO(BaseDAO):

    def get_unique_key(self):
        return "email"

    def get_model(self):
        return Faculty

    def get_label(self):
        return "Email"

    def get_where_clause(self, query, params):
        value = params.get("first_name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(first_name__istartswith=value.strip())

        return query