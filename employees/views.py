from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.contrib import messages

from .models import Department, Employees, Color
from .forms import EmployeeForm

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
    dept = get_object_or_404(Department, id=dept_id)   #get the departnet object

    #create modelformset to change multiple fields from multiple forms together    
    emps_formset = modelformset_factory(Employees, form=EmployeeForm, fields=('name', 'age', 'is_senior', 'favorite_color'), extra=0)
    #formset =  emps_formset(queryset=Employees.objects.filter(department=dept_id))

    if request.method == 'POST':
        formset =  emps_formset(request.POST)
        instances = formset.save()
        messages.info(request, 'Your Changes Have Been Commited')

    # prep the template
    
    formset =  emps_formset(queryset=Employees.objects.filter(department=dept_id))
    context = {
        'dept'      : dept,
        'formset'    : formset,
    }
    return render(request, 'employees/details.html', context)


# def details(request, dept_id):
#     dept = get_object_or_404(Department, id=dept_id)   #test
#     lst_of_emps = get_list_or_404(Employees, department=dept_id)

#     #create modelformset to change multiple filed  from multiple forms together
#     emps_formset = modelformset_factory(Employees, fields=('is_senior', 'favorite_color'))

#     context = {
#         'depts': dept,
#         'lst_of_emps': lst_of_emps,
#     }

#     return render(request, 'employees/details.html', context)
