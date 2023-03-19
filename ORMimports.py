from employees.models import Employees, Color, Department


# DROP ALL ITEMS IN THE TABLES
Employees.objects.all().delete()
Department.objects.all().delete()
Color.objects.all().delete()

#table generations
col_lst =[
    {'id' : 1, 'name' : 'Black'},
    {'id' : 2, 'name' : 'White'},
    {'id' : 3, 'name' : 'Blue'},
    {'id' : 4, 'name' : 'Green'},
    {'id' : 5, 'name' : 'Red'},
    {'id' : 6, 'name' : 'Pink'},
    {'id' : 7, 'name' : 'Yellow'},
]

dept_lst = [
    {'id' : 1, 'name' : 'Development'},
    {'id' : 2, 'name' : 'Finance'},
]

emp_lst = [
    {'id' : 1, 'name' : 'Moti',   'age':25, 'dept' : 1},
    {'id' : 2, 'name' : 'Eden',   'age':21, 'dept' : 1},
    {'id' : 3, 'name' : 'Liad',   'age':23, 'dept' : 1},
    {'id' : 4, 'name' : 'Karni',  'age':21, 'dept' : 1},
    {'id' : 5, 'name' : 'Matan',  'age':21, 'dept' : 2},
    {'id' : 6, 'name' : 'Guy',    'age':19, 'dept' : 2},
    {'id' : 7, 'name' : 'Tair',   'age':19, 'dept' : 2},
    {'id' : 8, 'name' : 'Lihi',   'age':19, 'dept' : 2},
]

for item in col_lst:
    a = Color.objects.create(id=item['id'], name=item['name'])
    print(str(a) + " added " + str(a.pk))
    a.save()
    print(str(a) + " saved\n")

for item in dept_lst:
    a = Department.objects.create(id=item['id'], name=item['name'])
    print(str(a) + " added " + str(a.pk))
    a.save()
    print(str(a) + " saved\n")


#DJANGO ORM requests the foreign key object
# dep_obj = [Development, Finance]
dep_obj = [Department.objects.get(name = 'Development'),
            Department.objects.get(name = 'Finance')]

for item in emp_lst:
    a = Employees.objects.create(id = item['id'], name=item['name'], age=item['age'], department=dep_obj[item['dept'] - 1]) #detp number starts with 1 and index starts at 0
    print(str(a) + " added " + str(a.pk))
    a.save()
    print(str(a) + " saved\n")
