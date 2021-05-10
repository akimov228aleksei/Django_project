"""Module containing API logic"""

from rest_framework import generics
from department.api.serializers.department import DepartmentCreateSerializer, DepartmentListSerializer
from department.DAO import DepartmentDAO


class DepartmentCreateView(generics.CreateAPIView):
    """Class for adding a department"""
    serializer_class = DepartmentCreateSerializer


class DepartmentListView(generics.ListAPIView):
    """Class for viewing all fields and id"""
    serializer_class = DepartmentListSerializer
    queryset = DepartmentDAO.get_list()


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Class for editing and deleting"""
    serializer_class = DepartmentCreateSerializer
    queryset = DepartmentDAO.get_list()
