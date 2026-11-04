from .base_dao import BaseDAO
from ..models import Marksheet
from ..utility.data_validator import DataValidator

class MarksheetDAO(BaseDAO):

    def get_unique_key(self):
        return "roll_number"

    def get_model(self):
        return Marksheet

    def get_label(self):
        return "Roll Number"

    def get_where_clause(self, query, params):
        value = params.get("student_name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(student_name__istartswith=value.strip())

        return query