from ..dao.marksheet_dao import MarksheetDAO
from ..service.base_service import BaseService


class MarksheetService(BaseService):

    def get_dao(self):
        return MarksheetDAO()