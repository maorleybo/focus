from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse

from .models import Department, Employees, Color

# Create your views here.

# homepage where you choose a department 
def index(request):
    lst_of_deps = Department.objects.order_by('id')   #get list of ids
    context = {'lst_of_deps' : lst_of_deps} 
    return render(request, 'employees/index.html', context)


def test(request):
    return HttpResponse("This is a Test!")


# show emps in the department once you chose a department 
def details(request, dept_id):
    dept = get_object_or_404(Department, id=dept_id)   #test
    lst_of_emps = get_list_or_404(Employees, department=dept_id)

    context = {
        'depts': dept,
        'lst_of_emps': lst_of_emps,
    }

    return render(request, 'employees/details.html', context)

#different approch

# def development(request):
#     return HttpResponse("<h1>Development department</h1>")


# def finance(request):
#     return HttpResponse("<h1>Finance department</h1>")

