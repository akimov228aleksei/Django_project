from department.models.department import Department
from department.models.employee import Employee


def dep_salary():

    dep_set = Department.objects.all()
    dep_list = []
    for i in dep_set:
        count = 1
        average = 1
        emp_set = Employee.objects.filter(dep__startswith=i)
        for k in emp_set:
            average += int(k.salary[:1])
            count += 1
        average = average / count
        j = (average, count)
        dep_list.append(j)
    return dep_list