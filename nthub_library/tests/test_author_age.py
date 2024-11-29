from datetime import datetime, timedelta
from odoo.addons.nthub_library.tests.common import TestPatientCommon
from odoo.tests import tagged
from odoo.exceptions import ValidationError


@tagged('post_install', '-at_install', 'author')
class TestPatientMethods(TestPatientCommon):

    def test_01_check_date_birth(self):
        with self.assertRaises(ValidationError):
            self.author.data_of_birth = datetime.today() + timedelta(days=1)
            self.author._check_date_birth()

    def test_02_check_date_birth(self):
        with self.assertRaises(ValidationError):
            self.author.data_of_birth = datetime.today() + timedelta(days=10)
            self.author._check_date_birth()
