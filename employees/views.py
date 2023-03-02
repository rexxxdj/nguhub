from django.conf import settings # import the settings file
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, QueryDict
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Category
from .forms import EmployeeCreateForm, EmployeeUpdateForm
from equipment.models import Equipment


def employee_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'employee/list.html'
    employees = Employee.objects.all()
    categories = Category.objects.all()
    sort_dict = (
        {'id':1, 'key':'rank','value':'Звання'},
        {'id':2, 'key':'lastname','value':'Прізвище'},
        {'id':3, 'key':'position','value':'Посада'},
        {'id':4, 'key':'category__name','value':'Локація'},
        )

    # Отримати параметри запиту GET
    category_filters = request.GET.getlist('category[]')
    sort_field = request.GET.get('sort', 'lastname')
    sort_order = request.GET.get('order', 'asc')
    
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
    template = 'employee/detail.html'
    employee = get_object_or_404(Employee, id=pk,)
    responsibleEquipment = Equipment.objects.filter(responsible=pk).order_by('category','name')
    fixedEquipment = Equipment.objects.filter(fixed=pk).order_by('category','name')
    employeeEquipment = Equipment.objects.filter(employee=pk).order_by('category','name')

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'employee': employee,
        'responsibleEquipment': responsibleEquipment,
        'fixedEquipment': fixedEquipment,
        'employeeEquipment': employeeEquipment
    }
    return render(request,template, context)


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee/add.html'
    form_class = EmployeeCreateForm

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        employee = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(EmployeeCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('employee:list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('employee:list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/update.html'
    form_class = EmployeeUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        employee = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{} {}\" було успішно змінено.'.format(employee.lastname, employee.firstname))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(EmployeeUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('employee:list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('employee:list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/confirm_delete.html'

    def get_success_url(self):
        if self.request.POST.get('_confirm'):
            messages.success(self.request, 'Користувача було успішно видалено.')
        if self.request.POST.get('_cancel'):
            messages.success(self.request, 'Ви відмінили запит на видалення')
        return reverse_lazy('employee:list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EmployeeDeleteView, self).post(request, *args, **kwargs)