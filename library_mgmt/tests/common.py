from datetime import datetime, timedelta
from odoo.tests.common import TransactionCase


class TestPatientCommon(TransactionCase):

    def setUp(self):
        super(TestPatientCommon, self).setUp()
        self.author = self.env['books.author'].create({
            'name': 'Test Author',
            'data_of_birth': datetime.today() - timedelta(days=365 * 30),
            })

        self.state = self.env['books.borrows'].create({
            'state': 'draft',
        })

        self.book = self.env['books.data'].create({
            'name': 'Test Book',
            'price': 10.0,
        })

        # Create mock copies and link them to the book
        self.copy_1 = self.env['book.copies'].create(
            {'book_id': self.book.id, 'state': 'available'})
        self.copy_2 = self.env['book.copies'].create(
            {'book_id': self.book.id, 'state': 'borrowed'})
        self.copy_3 = self.env['book.copies'].create(
            {'book_id': self.book.id, 'state': 'available'})