from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from department.models.department import Department
from department.models.employee import Employee
from department.views.department import DepartmentHome
from datetime import date


class DepartmentTest(TestCase):

    def setUp(self):

        self.department = Department.objects.create(
            name="some department"
        )

    def test_string_representation(self):
        department = Department(name='A sample name')
        self.assertEqual(str(department), department.name)

    def test_get_absolute_url(self):
        self.assertEqual(self.department.get_absolute_url(), '/')

    def test_update(self):
        response = self.client.post(reverse('department-update', args='1'), {
            'name': 'Updated name',
        })
        self.assertEqual(response.status_code, 302)

    def test_delete(self):
        response = self.client.post(
            reverse('department-delete', args='1'))
        self.assertEqual(response.status_code, 302)


class EmployeeTest(TestCase):

    def setUp(self):
        self.employee = Employee.objects.create(
            name_employee="some employee",
            salary=100,
            position="some position",
            date=date(2020, 2, 3),
        )


    def test_update(self):
        response = self.client.post(reverse('employee-update', args='1'), {
            'name_employee': 'Updated',
            'salary': 300,
            'position': 'Updated position',
            'date': date(2020, 3, 7),
        })
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.post(
            reverse('employee-delete', args='1'))
        self.assertEqual(response.status_code, 302)
