"""Serialization class file"""

from rest_framework import serializers
from department.models.employee import Employee


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name_employee', 'dep', 'salary', 'position', 'date']


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name_employee', 'dep', 'salary', 'position', 'date']
