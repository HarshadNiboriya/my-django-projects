from ..models import Marksheet
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class MarksheetService:

    def save(self, obj):
        print('marksheet service orm save()')
        duplicate = self.find_by_roll_number(obj.roll_number)

        if obj.id > 0:
            duplicate = duplicate.exclude(id=obj.id)

        if duplicate.exists():
            raise Exception('roll_number already exist')

        if obj.id == 0:
            obj.id = None

        obj.save()

    def get(self, pk):
        print('marksheet service orm get()')
        try:
            obj = Marksheet.objects.get(id=pk)
            return obj
        except Marksheet.DoesNotExist:
            return None

    def delete(self, id):
        print('marksheet service orm delete()')
        obj = self.get(id)
        obj.delete()

    def find_by_roll_number(self, roll_number):
        print('markseet service orm find_by_name()')
        obj = Marksheet.objects.filter(roll_number=roll_number)
        return obj

    def search(self, params):
        print('marksheet service orm search()')

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get('page_size', 0))

        query = Marksheet.objects.all()

        value = params.get("name", '')
        if DataValidator.is_not_null(value):
            query = query.filter(student_name__istartswith=value.strip())

        if (page_size == 0):
            return query

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_no - 1) * page_size

        return page_obj