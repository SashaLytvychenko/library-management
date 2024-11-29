# -*- coding: utf-8 -*-
'''

    Represents an author in the book management system.

    This class inherits from the 'models.Model' class provided by the Odoo framework.
    It extends the functionality of the base model to include additional fields and methods specific to authors.

    Attributes:
        _name (str): The technical name of the model.
        _inherit (list): A list of names of parent models to inherit from.
        _description (str): A description of the model.

    Fields:
        name (Char): The name of the author.
        date_of_birth (Date): The date of birth of the author.
        image (Image): An image representing the author.
        salary (Integer): The salary of the author.
        email (Char): The email address of the author.
        phone_number (Char): The phone number of the author.
        book_ids (Many2many): The books associated with the author.
        color (Integer): A color code for the author.
    Note:
        - The 'name' field is a required field.
        - The 'date_of_birth' field represents the birth date of the author.
        - The 'image' field stores an image file for the author.
        - The 'salary' field stores the salary of the author.
        - The 'email' field stores the email address of the author.
        - The 'phone_number' field stores the phone number of the author.
        - The 'book_ids' field establishes a many-to-many relationship with the 'books.data' model.
        - The 'color' field stores a color code for the author.
'''
from datetime import date
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Author(models.Model):
    _name = 'books.author'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'books.author'

    name = fields.Char(string="Name", tracking=True)
    data_of_birth = fields.Date(string="Date Of Birth")
    image = fields.Image(string="Image")
    age = fields.Integer(string="Age", compute='_compute_age')
    salary = fields.Integer(string="Salary")
    email = fields.Char(string='Email', size=256)
    phone_number = fields.Char(string='Phone Number', size=20)
    book_ids = fields.Many2many('books.data', string="Books")
    color = fields.Integer(string="color")
    start_date = fields.Datetime(default=fields.Datetime.today)
    end_date = fields.Date(string="End Date", store=True,
                           compute='_get_end_date_', inverse='_set_end_date')

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        """
            Sets the end date based on the start date and duration.

            This method calculates the end date by adding the duration (in days) to the start date.
            The calculated end date is then assigned to the 'end_date' field of the record.

            If either the start date or duration is not available, the function does nothing.

            Note: This method assumes that the 'start_date' and 'duration' fields are already populated.
            """
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        """
                Sets the duration based on the start date and end date.

                This method calculates the duration by subtracting the start date from the end date and adding 1 day.
                The calculated duration is then assigned to the 'duration' field of the record.

                If either the start date or end date is not available, the function does nothing.
                """
        for r in self:
            if not (r.start_date and r.duration):
                continue

            r.duration = (r.end_date - r.start_date).days + 1

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.data_of_birth:
                rec.age = today.year - rec.data_of_birth.year
            else:
                rec.age = 0

    DRAFT = 'draft'
    CANCEL = 'cancel'
    DONE = 'done'
    IN_CONSULTATION = 'in_consultation'

    @api.constrains('data_of_birth')
    def _check_date_birth(self):
        for record in self:
            if record.data_of_birth:
                self.validate_date_not_in_future(record.data_of_birth)

    @staticmethod
    def validate_date_not_in_future(date_of_birth):
        if date_of_birth > fields.Date.today():
            raise ValidationError(
                f'You cannot enter a birth date later than today: {fields.Date.today()}'
            )

    def set_state(self, state):
        for rec in self:
            rec.state = state

    def action_in_consultation(self):
        self.set_state(IN_CONSULTATION)

    def action_done(self):
        self.set_state(DONE)

    def action_cancel(self):
        self.set_state(CANCEL)

    def action_draft(self):
        self.set_state(DRAFT)

