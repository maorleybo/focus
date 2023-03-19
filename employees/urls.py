from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('test/', views.test, name = 'test'),
    # path('dev/', views.development, name = 'development'),
    # path('fin/', views.finance, name = 'finance'),

    path('dept/<int:dept_id>/', views.details, name = 'details'),

]