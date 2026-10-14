from django.db import connection

from ..models import Course
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class CourseService:

    def save(self, obj):
        print('course service orm save()')
        duplicate = self.find_by_name(obj.name)

        if obj.id > 0:
            duplicate = duplicate.exclude(id=obj.id )

        if duplicate.exists():
            raise Exception('course Name already exist')

        if obj.id == 0:
            obj.id = None

        obj.save()

    def get(self, pk):
        print('Course service orm get()')
        try:
            obj = Course.objects.get(id=pk)
            return obj
        except Course.DoesNotExist:
            return None

    def delete(self, id):
        print('Course service orm delete()')
        obj = self.get(id)
        obj.delete()

    def find_by_name(self, name):
        print('Course service orm find_by_name()')
        obj = Course.objects.filter(name=name)
        return obj

    def search(self, params):
        print('Course service orm search()')

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get('page_size', 0))

        query = Course.objects.all()

        value = params.get("name", '')
        if DataValidator.is_not_null(value):
            query = query.filter(name__istartswith=value.strip())

        if (page_size == 0):
            return query

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_no - 1) * page_size

        return page_obj