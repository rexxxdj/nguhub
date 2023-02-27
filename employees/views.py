from django.conf import settings # import the settings file
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, QueryDict
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee, Category
from .forms import EmployeeForm
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
        {'id':4, 'key':'category__name','value':'Категорія'},
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
    equipments = Equipment.objects.filter(employee=pk).order_by('category','name')

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'employee': employee,
        'equipments': equipments
    }
    return render(request,template, context)

def employee_add(request):
    if request.method == 'POST':        
        form = EmployeeForm(request.POST, request.FILES)
        if request.POST.get('_save'):
            if form.is_valid():
                print("VALID")
                form.save()
                messages.success(request, 'Дані було успішно збережено.')
            else:
                print("NOT VALID")
        return redirect('employee:list')
    else:
        form = EmployeeForm()

    ranks = (
        {'id': u'сл.', 'name': u"Службовець"},
        {'id': u'солд.', 'name': u"Солдат"},
        {'id': u'ст.солд.', 'name': u"Старший солдат"},
        {'id': u'мол.с-нт', 'name': u"Молодший сержант"},
        {'id': u'с-нт', 'name': u"Сержант"},
        {'id': u'ст.с-нт', 'name': u"Старший сержант"},
        {'id': u'гол.с-нт', 'name': u"Головний сержант"},
        {'id': u'шт.с-нт', 'name': u"Штаб-сержант"},
        {'id': u'м.с-нт', 'name': u"Майстер-сержант"},
        {'id': u'ст.м.с-нт', 'name': u"Старший майстер-сержант"},
        {'id': u'гол.м.с-нт', 'name': u"Головний майстер-сержант"},
        {'id': u'мол.л-нт', 'name': u"Молодший лейтенант"},
        {'id': u'л-нт', 'name': u"Лейтенант"},
        {'id': u'ст.л-нт', 'name': u"Старший лейтенант"},
        {'id': u'к-н', 'name': u"Капітан"},
        {'id': u'м-р', 'name': u"Майор"},
        {'id': u'п/п-к', 'name': u"Підполковник"},
        {'id': u'п-к', 'name': u"Полковник"},
        {'id': u'бриг.ген.', 'name': u"Бригадний генерал"},
        {'id': u'ген.м-р', 'name': u"Генерал-майор"},
        {'id': u'ген.л-нт', 'name': u"Генерал-лейтенант"},
        {'id': u'ген.', 'name': u"Генерал"}
    )
    categories = Category.objects.all()
    context = {
        'ranks': ranks,
        'categories': categories,
        'form': form
    }
    return render(request, 'employee/add.html', context)


def employee_update(request, pk):
    employee = get_object_or_404(Employee, id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if request.POST.get('_save'):
            if form.is_valid():
                form.save()
                messages.success(request, '\"{}\" було успішно змінено.'.format(employee.fullname))
        if request.POST.get('_dismiss'):
            messages.success(request, 'Ви відмінили запит на зміну \"{}\".'.format(employee.fullname))
        return redirect('employee:list')
    else:
        form = EmployeeForm(instance=employee)


    ranks = (
        {'id': u'сл.', 'name': u"Службовець"},
        {'id': u'солд.', 'name': u"Солдат"},
        {'id': u'ст.солд.', 'name': u"Старший солдат"},
        {'id': u'мол.с-нт', 'name': u"Молодший сержант"},
        {'id': u'с-нт', 'name': u"Сержант"},
        {'id': u'ст.с-нт', 'name': u"Старший сержант"},
        {'id': u'гол.с-нт', 'name': u"Головний сержант"},
        {'id': u'шт.с-нт', 'name': u"Штаб-сержант"},
        {'id': u'м.с-нт', 'name': u"Майстер-сержант"},
        {'id': u'ст.м.с-нт', 'name': u"Старший майстер-сержант"},
        {'id': u'гол.м.с-нт', 'name': u"Головний майстер-сержант"},
        {'id': u'мол.л-нт', 'name': u"Молодший лейтенант"},
        {'id': u'л-нт', 'name': u"Лейтенант"},
        {'id': u'ст.л-нт', 'name': u"Старший лейтенант"},
        {'id': u'к-н', 'name': u"Капітан"},
        {'id': u'м-р', 'name': u"Майор"},
        {'id': u'п/п-к', 'name': u"Підполковник"},
        {'id': u'п-к', 'name': u"Полковник"},
        {'id': u'бриг.ген.', 'name': u"Бригадний генерал"},
        {'id': u'ген.м-р', 'name': u"Генерал-майор"},
        {'id': u'ген.л-нт', 'name': u"Генерал-лейтенант"},
        {'id': u'ген.', 'name': u"Генерал"}
    )
    categories = Category.objects.all()
    context = {
        'employee': employee,
        'categories': categories,
        'ranks': ranks,
        'form': form
    }
    return render(request, 'employee/update.html', context)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('employee:list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EmployeeDeleteView, self).post(request, *args, **kwargs)