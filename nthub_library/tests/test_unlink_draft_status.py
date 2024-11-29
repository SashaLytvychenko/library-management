from odoo.exceptions import ValidationError
from odoo.addons.nthub_library.tests.common import TestPatientCommon
from odoo.tests import tagged


@tagged('post_install', '-at_install', 'state')
class TestRepairDeadlineMethods(TestPatientCommon):

    def test_01_check_unlink_draft_status(self):
        with self.assertRaises(ValidationError):
            self.state.state = 'running'
            self.state.unlink()

    def test_02_check_unlink_draft_status(self):
        with self.assertRaises(ValidationError):
            self.state.state = 'delayed'
            self.state.unlink()

    def test_03_check_unlink_draft_status(self):
        with self.assertRaises(ValidationError):
            self.state.state = 'ended'
            self.state.unlink()
