import json
from django.test import TestCase
from django.urls import reverse
from department.models.department import Department
from department.api.serializers.department import DepartmentListSerializer, DepartmentCreateSerializer


class TestDepartmentAPI(TestCase):

    def setUp(self):
        self.department = Department.objects.create(name='Some API department_1')
        self.department = Department.objects.create(name='Some API department_2')

    def test_get_all_departments(self):
        response = self.client.get(reverse('department-api-list'))
        department = Department.objects.all()
        serializer = DepartmentListSerializer(department, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_get_detail_departments(self):
        response = self.client.get(reverse('department-api-detail', kwargs={'pk': self.department.pk}))
        department = Department.objects.get(pk=self.department.pk)
        serializer = DepartmentCreateSerializer(department)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_detail_departments(self):
        response = self.client.get(reverse('department-api-detail', kwargs={'pk': self.department.pk+1}))
        self.assertEqual(response.status_code, 404)

    def test_create_valid_data(self):
        valid_data = {
            'name': 'valid data'
        }
        response = self.client.post(reverse('department-api-create'),
                                    data=json.dumps(valid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_invalid_data(self):
        invalid_data = {
            'name': ''
        }
        response = self.client.post(reverse('department-api-create'),
                                    data=json.dumps(invalid_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_valid_data(self):
        valid_data = {
            'name': 'update valid data'
        }
        response = self.client.put(reverse('department-api-detail', kwargs={'pk': self.department.pk}),
                                   data=json.dumps(valid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_invalid_data(self):
        invalid_data = {
            'name': ''
        }
        response = self.client.put(reverse('department-api-detail', kwargs={'pk': self.department.pk}),
                                   data=json.dumps(invalid_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_valid_data(self):
        response = self.client.delete(reverse('department-api-detail', kwargs={'pk': self.department.pk}))
        self.assertEqual(response.status_code, 204)

    def test_delete_invalid_data(self):
        response = self.client.delete(reverse('department-api-detail', kwargs={'pk': self.department.pk+1}))
        self.assertEqual(response.status_code, 404)