"""Module containing API logic"""

from rest_framework import generics
from department.api.serializers.employee import EmployeeCreateSerializer, EmployeeListSerializer
from department.DAO import EmployeeDAO


class EmployeeCreateView(generics.CreateAPIView):
    """Class for adding employee"""
    serializer_class = EmployeeCreateSerializer


class EmployeeListView(generics.ListAPIView):
    """Class for viewing all fields and id"""
    serializer_class = EmployeeListSerializer
    queryset = EmployeeDAO.get_list()


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Class for editing and deleting"""
    serializer_class = EmployeeCreateSerializer
    queryset = EmployeeDAO.get_list()
