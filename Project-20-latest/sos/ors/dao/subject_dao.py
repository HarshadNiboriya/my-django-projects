from .base_dao import BaseDAO
from ..models import Subject
from ..utility.data_validator import DataValidator


class SubjectDAO(BaseDAO):

    def get_unique_key(self):
        return "name"

    def get_model(self):
        return Subject

    def get_label(self):
        return "Subject Name"

    def get_where_clause(self, query, params):
        value = params.get("name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(name__istartswith=value.strip())

        return query