"""The file contains all the available methods
for accessing the database"""
from department.models import department, employee, vacation


class DepartmentDAO:
    """The class contains methods for accessing the department table"""

    @staticmethod
    def get_list():
        """The method returns all data from the department table"""
        return department.Department.objects.all()


class EmployeeDAO:
    """The class contains methods for accessing the employee table"""

    @staticmethod
    def get_list():
        """The method returns all data from the employee table"""
        return employee.Employee.objects.all()

    @staticmethod
    def filter_dep(value):
        """The method returns all employees belonging to a specific department"""
        response = employee.Employee.objects.filter(dep=value)
        return response


class VacationDAO:
    """The class contains methods for accessing the vacation table"""

    @staticmethod
    def get_list():
        """The method returns all data from the vacation table"""
        return vacation.Vacation.objects.all()
