from django.urls import path

from . import views


app_name = 'employees'  # namespace of the app for scalability
urlpatterns = [
    path('', views.index, name = 'index'),  # the homepage of employees
    path('dept/<int:dept_id>/', views.details, name = 'details'),
]