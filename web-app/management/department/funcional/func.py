from department.models.department import Department

def dep_select():

    dep_set = []
    department = Department.objects.all()

    for i in department:
        a = (i, i)
        dep_set.append(a)

    return dep_set
