from odoo.exceptions import ValidationError
from odoo.addons.nthub_library.tests.common import TestPatientCommon
from odoo.tests import tagged


@tagged('post_install', '-at_install', 'book')
class TestRepairDeadlineMethods(TestPatientCommon):

    def test_compute_copy_count(self):
        self.book._compute_copy_count()
        self.assertEqual(
            int(self.book.copy_count),
            3,
            "The computed copy_count should match the number of related copy_ids records."
        )