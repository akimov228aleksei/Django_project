from django.test import TestCase
from department.models.department import Department


class DepartmentTest(TestCase):

    def setUp(self):

        self.department = Department.objects.create(
            name="some department"
        )

    def test_label(self):
        department = Department.objects.get(id=1)
        field_label = department._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Department:')