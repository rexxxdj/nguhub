from django.conf import settings # import the settings file
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, QueryDict, JsonResponse
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Equipment, Status, Category
from employees.models import Employee
from .forms import EquipmentForm


def equipment_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'equipment/list.html'
    equipments = Equipment.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    employees = Employee.objects.all()
    sort_dict = (
        {'id':1, 'key':'name','value':'Назва'},
        {'id':2, 'key':'category__name','value':'Категорія'},
        {'id':3, 'key':'operationDate','value':'Дата вв. в експлуатацію'},
        {'id':4, 'key':'status__name','value':'Статус'},
        {'id':5, 'key':'location__name','value':'Місце закріплення'},
        {'id':6, 'key':'responsible__lastname','value':'Матеріально Відповідальний'},
        {'id':7, 'key':'fixed__lastname','value':'За ким закріплено'},
        {'id':6, 'key':'employee__lastname','value':'Користувач'},
        )

    # Отримати параметри запиту GET
    category_filters = request.GET.getlist('category[]')
    status_filters = request.GET.getlist('status[]')
    sort_field = request.GET.get('sort', 'id')
    sort_order = request.GET.get('order', 'desc')
    
    # Фільтрувати дані за категорією
    if category_filters:
        equipments = equipments.filter(category__name__in=category_filters)
    
    # Фільтрувати дані за статусом
    if status_filters:
        equipments = equipments.filter(status__name__in=status_filters)
    
    # Сортувати дані за вибраним полем
    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    equipments = equipments.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'equipments': equipments,
        'categories': categories,
        'statuses': statuses,
        'employees': employees,
        'selected_categories':category_filters,
        'selected_statuses':status_filters,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order
    }
    return render(request, template, context)


def equipment_detail(request, pk):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'equipment/detail.html'
    equipment = get_object_or_404(Equipment, id=pk)

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'equipment': equipment
    }
    return render(request,template, context)

def equipment_add(request):
    if request.method == 'POST':        
        form = EquipmentForm(request.POST, request.FILES)
        if request.POST.get('_save'):
            if form.is_valid():
                form.save()
                messages.success(request, 'Дані було успішно збережено.')
        return redirect('equipment:list')
    else:
        form = EquipmentForm()

    categories = Category.objects.all()
    statuses = Status.objects.all()
    employees = Employee.objects.all()
    context = {
        'categories': categories,
        'statuses': statuses,
        'employees': employees,
        'form': form
    }
    return render(request, 'equipment/add.html', context)


def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, id=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if request.POST.get('_save'):
            if form.is_valid():
                form.save()
                messages.success(request, '\"{}\" було успішно змінено.'.format(equipment.name))
        if request.POST.get('_dismiss'):
            messages.success(request, 'Ви відмінили запит на зміну \"{}\".'.format(equipment.name))
        return redirect('equipment:list')
    else:
        form = EquipmentForm(instance=equipment)

    categories = Category.objects.all()
    statuses = Status.objects.all()
    employees = Employee.objects.all()
    context = {
        'equipment': equipment,
        'categories': categories,
        'statuses': statuses,
        'employees': employees,
        'form': form
    }
    return render(request, 'equipment/update.html', context)


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'equipment/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('equipment:list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EquipmentDeleteView, self).post(request, *args, **kwargs)