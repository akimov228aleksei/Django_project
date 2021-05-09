from django.test import TestCase
from department.models.department import Department
from department.models.employee import Employee
from department.models.vacation import Vacation
from datetime import date


class DepartmentTest(TestCase):

    def setUp(self):

        self.department = Department.objects.create(
            name="some department")

    def test_label(self):
        department = Department.objects.get(id=self.department.pk)
        field_label = department._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Department:')

    def test_unique(self):
        department = Department.objects.get(id=self.department.pk)
        unique = department._meta.get_field('name').unique
        self.assertTrue(unique)

    def test_max_length(self):
        department = Department.objects.get(id=self.department.pk)
        max_length = department._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_get_absolute_url(self):
        self.assertEqual(self.department.get_absolute_url(), '/')

    def test_string_representation(self):
        department = Department(name='A sample name')
        self.assertEqual(str(department), department.name)

    def test_content(self):
        self.assertEqual(f'{self.department.name}', 'some department')

    def test_salary(self):
        SALARY = [100, 150, 200, 250, 300, 350, 400, 450, 500]
        salary = []
        for i in range(100, 1000, 100):
            self.employee = Employee.objects.create(
                name_employee=f"employee-{i}",
                dep=self.department,
                salary=i,
                position="some position",
                date=date(2020, 2, 3),
            )
            salary.append(self.department.salary)

        self.assertEqual(SALARY, salary)

    def test_amount(self):
        for i in range(1, 10):
            self.employee = Employee.objects.create(
                name_employee=f"employee-{i}",
                dep=self.department,
                salary=100,
                position="some position",
                date=date(2020, 2, 3),
            )
            self.assertEqual(self.department.amount, i)


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

    def test_label(self):
        employee = Employee.objects.get(id=self.employee.pk)
        field_label = employee._meta.get_field('name_employee').verbose_name
        self.assertEqual(field_label, 'Employee:')
        field_label = employee._meta.get_field('dep').verbose_name
        self.assertEqual(field_label, 'dep')
        field_label = employee._meta.get_field('salary').verbose_name
        self.assertEqual(field_label, 'Salary:')
        field_label = employee._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'Position:')
        field_label = employee._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'Date:')

    def test_unique(self):
        employee = Employee.objects.get(id=self.employee.pk)
        unique = employee._meta.get_field('name_employee').unique
        self.assertTrue(unique)

    def test_max_length(self):
        employee = Employee.objects.get(id=self.employee.pk)
        max_length = employee._meta.get_field('name_employee').max_length
        self.assertEqual(max_length, 30)
        max_length = employee._meta.get_field('position').max_length
        self.assertEqual(max_length, 30)

    def test_get_absolute_url(self):
        self.assertEqual(self.employee.get_absolute_url(), '/employee/')

    def test_string_representation(self):
        employee = Employee(name_employee='A sample name')
        self.assertEqual(str(employee), employee.name_employee)

    def test_content(self):
        self.assertEqual(f'{self.employee.name_employee}', 'some employee')
        self.assertEqual(f'{self.employee.dep}', 'some department')
        self.assertEqual(f'{self.employee.salary}', '100')
        self.assertEqual(f'{self.employee.position}', 'some position')
        self.assertEqual(f'{self.employee.date}', '2020-02-03')


class VacationTest(TestCase):

    def setUp(self):

        self.employee = Employee.objects.create(
            name_employee="some employee",
            salary=100,
            date=date(2020, 2, 3),
        )
        self.vacation = Vacation.objects.create(
            name_vacation=self.employee,
            date1=date(2020, 3, 3),
            date2=date(2020, 4, 4)
        )

    def test_label(self):
        vacation = Vacation.objects.get(id=self.vacation.pk)
        field_label = vacation._meta.get_field('date1').verbose_name
        self.assertEqual(field_label, 'Date start:')
        field_label = vacation._meta.get_field('date2').verbose_name
        self.assertEqual(field_label, 'Date end:')

    def test_get_absolute_url(self):
        self.assertEqual(self.vacation.get_absolute_url(), '/vacation/')

    def test_string_representation(self):
        vacation = Vacation(name_vacation=self.employee)
        self.assertEqual(str(vacation), f'{vacation.name_vacation}')

    def test_content(self):
        self.assertEqual(f'{self.vacation.name_vacation}', 'some employee')
        self.assertEqual(f'{self.vacation.date1}', '2020-03-03')
        self.assertEqual(f'{self.vacation.date2}', '2020-04-04')
