"""Serialization class file"""

from rest_framework import serializers
from department.models.vacation import Vacation


class VacationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ['id', 'name_vacation', 'date1', 'date2']

    def validate(self, data):

        if data['date2'] <= data['date1']:
            raise serializers.ValidationError("End date cannot be earlier than start date")
        return data


class VacationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ['id', 'name_vacation', 'date1', 'date2']
