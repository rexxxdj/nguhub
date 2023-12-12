from django.conf import settings # import the settings file
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict, JsonResponse
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Equipment, Status, Category
from employee.models import Employee
from .forms import EquipmentCreateForm, EquipmentUpdateForm

@login_required(login_url="/")
def equipment_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'equipment/list.html'
    #template = 'employee/list.html'
    equipments = Equipment.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    employees = Employee.objects.all()

    sort_dict = (
        {'id':1, 'key':'inventory_name','value':'Номенклатурна назва'},
        {'id':2, 'key':'category__name','value':'Категорія'},
        {'id':3, 'key':'status__name','value':'Статус'},
        {'id':4, 'key':'inventory_number', 'value':u'Інвентарний номер'},
        {'id':5, 'key':'serial_number', 'value':'Серійний номер'},
        {'id':6, 'key':'counterparty__name','value':'Контрагент'},
        )

    # Отримати параметри запиту GET
    category_filters = request.GET.getlist('category[]')
    status_filters = request.GET.getlist('status[]')
    sort_field = request.GET.get('sort', 'inventory_name')
    sort_order = request.GET.get('order', 'asc')
    search_query = request.GET.get('q', '')
    
    # Фільтрувати дані за категорією
    if category_filters:
        equipments = equipments.filter(category__name__in=category_filters)
    
    # Фільтрувати дані за статусом
    if status_filters:
        equipments = equipments.filter(status__name__in=status_filters)

    # Фільтрувати дані за пошуком
    if search_query:
        equipments = equipments.filter(
                    Q(inventory_name__icontains=search_query) |
                    Q(inventory_number__icontains=search_query) |
                    Q(serial_number__icontains=search_query) |
                    Q(counterparty__name__icontains=search_query)
                    )
    
    # Сортувати дані за вибраним полем
    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    equipments = equipments.order_by(ordering)


    pagination_number = 50
    paginator = Paginator(equipments, pagination_number)
    page_number = request.GET.get('page')  # отримати номер сторінки з запиту GET параметром

    try:
        equipments = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        equipments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        equipments = paginator.page(paginator.num_pages)

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
        'sort_order': sort_order,
        'search_query': search_query,
        'pagination_number': pagination_number,
        'page_number': page_number
    }
    return render(request, template, context)


@login_required(login_url="/")
def equipment_detail(request, pk):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'equipment/detail.html'
    equipment = get_object_or_404(Equipment, id=pk)
    elements = Equipment.objects.all().filter(destinationEquipment=pk)
    history = equipment.history.all().order_by('history_date')

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'equipment': equipment,
        'elements':elements,
        'history': history
    }
    return render(request,template, context)


class EquipmentCreateView(CreateView):
    model = Equipment
    template_name = 'equipment/add.html'
    form_class = EquipmentCreateForm

    def get_context_data(self, **kwargs):
        context = super(EquipmentCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(EquipmentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('equipment:list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = 'equipment/update.html'
    form_class = EquipmentUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(EquipmentUpdateView, self).get_context_data(**kwargs)
        context['return_path'] = self.request.META.get('HTTP_REFERER','/')
        return context

    def form_valid(self, form):        
        equipment = self.get_object()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(equipment.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(EquipmentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return self.request.POST.get('return_path')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


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
def equipment_history_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'equipment/history_list.html'
    history = Equipment.history.filter(history_type='-')

    context = {
        'history': history
    }
    return render(request, template, context)