"""Serialization class file"""

from rest_framework import serializers
from department.models.department import Department


class DepartmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'salary', 'amount']


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'salary', 'amount']
