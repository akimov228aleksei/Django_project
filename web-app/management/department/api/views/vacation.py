"""Module containing API logic"""

from rest_framework import generics
from department.api.serializers.vacation import VacationCreateSerializer, VacationListSerializer
from department.DAO import VacationDAO


class VacationCreateView(generics.CreateAPIView):
    """Class for adding vacation"""
    serializer_class = VacationCreateSerializer


class VacationListView(generics.ListAPIView):
    """Class for viewing all fields and id"""
    serializer_class = VacationListSerializer
    queryset = VacationDAO.get_list()


class VacationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Class for editing and deleting"""
    serializer_class = VacationCreateSerializer
    queryset = VacationDAO.get_list()
