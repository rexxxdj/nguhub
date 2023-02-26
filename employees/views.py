from django.conf import settings # import the settings file
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, QueryDict
from urllib.parse import urlencode
from django.views.generic import ListView
from .models import Employee, Category


def employee_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'employee_list.html'
    employees = Employee.objects.all()
    categories = Category.objects.all()
    sort_dict = (
        {'id':1, 'key':'rank','value':'Звання'},
        {'id':2, 'key':'lastname','value':'Прізвище'},
        {'id':3, 'key':'position','value':'Посада'},
        {'id':4, 'key':'category__name','value':'Категорія'},
        )

    # Отримати параметри запиту GET
    category_filters = request.GET.getlist('category[]')
    sort_field = request.GET.get('sort', 'lastname')
    sort_order = request.GET.get('order', 'asc')

    print(category_filters)
    
    # Фільтрувати дані за категорією
    if category_filters:
        employees = employees.filter(category__name__in=category_filters)
    
    # Сортувати дані за вибраним полем
    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    employees = employees.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'employees': employees,
        'categories': categories,
        'selected_categories':category_filters,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order
    }
    return render(request, template, context)


def employee_detail(request, pk):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'employee_detail.html'
    employee = get_object_or_404(Employee, id=pk,)

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'employee': employee
    }
    return render(request,template, context)

def employee_add(request):
    return HttpResponse('<h1>Employee Add Form</h1>')

def employee_edit(request, sid):
    return HttpResponse('<h1>Edit Employee %s</h1>' % sid)

def employee_delete(request, sid):
    return HttpResponse('<h1>Delete Employee %s</h1>' % sid)