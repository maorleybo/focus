from django.shortcuts import render
from django.http import HttpResponse

from .models import Department

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
    strg = "<h1>details for dept %s</h1>"
    return HttpResponse(strg % dept_id)

#different approch

# def development(request):
#     return HttpResponse("<h1>Development department</h1>")


# def finance(request):
#     return HttpResponse("<h1>Finance department</h1>")

