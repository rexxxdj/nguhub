from django.conf import settings # import the settings file
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Employee
from .forms import EmployeeCreateForm, EmployeeUpdateForm
from nguhub.models import Location, Placement


@login_required(login_url="/")
def employee_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'employee/list.html'
    employees = Employee.objects.all()
    placements = Placement.objects.all()
    sort_dict = (
        {'id':1, 'key':'rank','value':'Звання'},
        {'id':2, 'key':'lastname','value':'Прізвище'},
        {'id':3, 'key':'position','value':'Посада'},
        {'id':4, 'key':'placement__name','value':'Локація'},
        )

    # Отримати параметри запиту GET
    placement_filters = request.GET.getlist('placement[]')
    sort_field = request.GET.get('sort', 'lastname')
    sort_order = request.GET.get('order', 'asc')
    search_query = request.GET.get('q', '')
    
    # Фільтрувати дані за категорією
    if placement_filters:
        employees = employees.filter(placement__name__in=placement_filters)
    
    # Фільтрувати дані за пошуком
    if search_query:
        employees = employees.filter(
                    Q(firstname__icontains=search_query) |
                    Q(lastname__icontains=search_query) |
                    Q(position__icontains=search_query)
                    )

    # Сортувати дані за вибраним полем
    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    employees = employees.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'employees': employees,
        'placements': placements,
        'selected_placements':placement_filters,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order,
        'search_query': search_query
    }
    return render(request, template, context)


@login_required(login_url="/")
def employee_detail(request, pk):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'employee/detail.html'
    employee = get_object_or_404(Employee, id=pk,)
    #responsibleEquipment = Equipment.objects.filter(responsible=pk).order_by('category','name')
    #fixedEquipment = Equipment.objects.filter(fixed=pk).order_by('category','name')
    #employeeEquipment = Equipment.objects.filter(employee=pk).order_by('category','name')
    history = employee.history.all().order_by('history_date')

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'employee': employee,
        #'responsibleEquipment': responsibleEquipment,
        #'fixedEquipment': fixedEquipment,
        #'employeeEquipment': employeeEquipment,
        'history': history
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


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
        employee = self.get_object()
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")



'''  History   '''
@login_required(login_url="/")
def employee_history_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'employee/history_list.html'
    history = Employee.history.filter(history_type='-')
    context = {
        'history': history
    }
    return render(request, template, context)