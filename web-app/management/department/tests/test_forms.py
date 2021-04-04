from django.test import TestCase
from department.forms.department import DepartmentForm
from department.forms.employee import EmployeeForm
from department.forms.vacation import VacationForm
from datetime import date


class DepartmentTest(TestCase):

    def test_label(self):
        form = DepartmentForm()
        self.assertEqual(form.fields['name'].label, 'Department:')


class EmployeeTest(TestCase):

    def test_label(self):
        form = EmployeeForm()
        self.assertEqual(form.fields['name_employee'].label, 'Employee:')
        self.assertEqual(form.fields['dep'].label, 'Dep')
        self.assertEqual(form.fields['salary'].label, 'Salary:')
        self.assertEqual(form.fields['position'].label, 'Position:')
        self.assertEqual(form.fields['date'].label, 'Date:')


class VacationTest(TestCase):

    def test_label(self):
        form = VacationForm()
        self.assertEqual(form.fields['name_vacation'].label, 'Name vacation')
        self.assertEqual(form.fields['date1'].label, 'Date start:')
        self.assertEqual(form.fields['date2'].label, 'Date end:')

    # def test_date(self):
    #     date1 = date(2020, 1, 1)
    #     date2 = date(2021, 1, 1)
    #     form = VacationForm(data={'date1': date1, 'date2': date2})
    #     self.assertTrue(form.is_valid())
