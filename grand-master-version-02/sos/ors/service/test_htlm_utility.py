import os
import sys
import django

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

sys.path.insert(0, BASE_DIR)

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'sos.settings'
)

django.setup()

from ors.models import Role
from ors.service.role_service import RoleService
from ors.utility.html_utility import HtmlUtility

role_list = RoleService().search({})

html = HtmlUtility.get_list_from_beans(
    "roleId",
    1,
    role_list
)

print(html)
