from django.test import TestCase, RequestFactory
from django.urls import reverse
from department.models.department import Department
from department.models.employee import Employee
from department.models.vacation import Vacation
from department.views.department import DepartmentHome
from department.views.employee import EmployeeHome
from department.views.vacation import VacationHome
from datetime import date


class DepartmentTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(
            name="some department"
        )

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department.html')

    def test_update(self):
        response = self.client.post(reverse('department-update', args=f'{self.department.pk}'), {
            'name': 'Updated name',
        })
        self.assertEqual(response.status_code, 302)
        self.department.refresh_from_db()
        self.assertEqual(f'{self.department.name}', 'Updated name')

    def test_delete(self):
        response = self.client.post(reverse('department-delete', args=f'{self.department.pk}'))
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('department-delete', args=f'{self.department.pk}'))
        self.assertEqual(response.status_code, 404)


class EmployeeTest(TestCase):

    def setUp(self):

        self.department = Department.objects.create(
            name="some department"
        )
        self.employee = Employee.objects.create(
            name_employee="some employee",
            dep=self.department,
            salary=100,
            position="some position",
            date=date(2020, 2, 3),
        )

    def test_home(self):
        response = self.client.get(reverse('employee_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee.html')

    def test_update(self):
        response = self.client.post(reverse('employee-update', kwargs={"pk": self.employee.pk}), {
            'name_employee': 'Updated',
            'dep': self.department.pk,
            'salary': 300,
            'position': 'Updated position',
            'date': date(2020, 3, 7),
        })
        self.assertEqual(response.status_code, 302)
        self.employee.refresh_from_db()
        self.assertEqual(f'{self.employee.name_employee}', 'Updated')

    def test_delete(self):
        response = self.client.post(reverse('employee-delete', args=f'{self.employee.pk}'))
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('employee-delete', args=f'{self.employee.pk}'))
        self.assertEqual(response.status_code, 404)


class VacationTest(TestCase):

    def setUp(self):

        self.employee = Employee.objects.create(
            name_employee="some employee",
            salary=100,
            date=date(2020, 2, 3)
        )

        self.vacation = Vacation.objects.create(
            name_vacation=self.employee,
            date1=date(2020, 3, 3),
            date2=date(2020, 4, 4)
        )

    def test_home(self):
        response = self.client.get(reverse('vacation_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacation/vacation.html')

    def test_update(self):
        response = self.client.post(reverse('vacation-update', args=f'{self.vacation.pk}'), {
            'name_vacation': self.employee,
            'date1': date(2019, 1, 1),
            'date2': date(2020, 3, 7),
        })
        self.assertEqual(response.status_code, 302)
        self.vacation.refresh_from_db()
        self.assertEqual(f'{self.vacation.name_vacation}', f'{self.employee}')
        self.assertEqual(f'{self.vacation.date1}', '2019-01-01')
        self.assertEqual(f'{self.vacation.date2}', '2020-03-07')

    def test_delete(self):
        response = self.client.post(reverse('vacation-delete', args=f'{self.vacation.pk}'))
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('vacation-delete', args=f'{self.vacation.pk}'))
        self.assertEqual(response.status_code, 404)
