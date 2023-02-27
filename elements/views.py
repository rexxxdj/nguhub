from django.conf import settings # import the settings file
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, QueryDict
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Element, Status, Category
from .forms import ElementForm
from equipment.models import Equipment


def element_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'element/list.html'
    elements = Element.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    equipments = Equipment.objects.all()
    sort_dict = (
        {'id':1, 'key':'name','value':'Назва'},
        {'id':2, 'key':'category__name','value':'Категорія'},
        {'id':3, 'key':'status__name','value':'Статус'},
        {'id':4, 'key':'equipment__name','value':'Де встановлено'}
        )

    # Отримати параметри запиту GET
    category_filters = request.GET.getlist('category[]')
    status_filters = request.GET.getlist('status[]')
    sort_field = request.GET.get('sort', 'name')
    sort_order = request.GET.get('order', 'asc')
    
    # Фільтрувати дані за категорією
    if category_filters:
        elements = elements.filter(category__name__in=category_filters)
    
    # Фільтрувати дані за статусом
    if status_filters:
        elements = elements.filter(status__name__in=status_filters)
    
    # Сортувати дані за вибраним полем
    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    elements = elements.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'elements': elements,
        'categories': categories,
        'statuses': statuses,
        'equipments': equipments,
        'selected_categories':category_filters,
        'selected_statuses':status_filters,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order
    }
    return render(request, template, context)


def element_detail(request, pk):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'element/detail.html'
    element = get_object_or_404(Element, id=pk,)

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'element': element
    }
    return render(request, template, context)

def element_add(request):
    if request.method == 'POST':        
        form = ElementForm(request.POST, request.FILES)
        if request.POST.get('_save'):
            if form.is_valid():
                form.save()
                messages.success(request, 'Дані було успішно збережено.')
        return redirect('element:list')
    else:
        form = ElementForm()

    categories = Category.objects.all()
    statuses = Status.objects.all()
    equipments = Equipment.objects.all()
    context = {
        'categories': categories,
        'statuses': statuses,
        'equipments': equipments,
        'form': form
    }
    return render(request, 'element/add.html', context)


def element_update(request, pk):
    element = get_object_or_404(Element, id=pk)
    if request.method == 'POST':
        form = ElementForm(request.POST, request.FILES, instance=element)
        if request.POST.get('_save'):
            if form.is_valid():
                form.save()
                messages.success(request, '\"{}\" було успішно змінено.'.format(element.name))
        if request.POST.get('_dismiss'):
            messages.success(request, 'Ви відмінили запит на зміну \"{}\".'.format(element.name))
        return redirect('element:list')
    else:
        form = ElementForm(instance=element)

    categories = Category.objects.all()
    statuses = Status.objects.all()
    equipments = Equipment.objects.all()
    context = {
        'element': element,
        'categories': categories,
        'statuses': statuses,
        'equipments': equipments,
        'form': form
    }
    return render(request, 'element/update.html', context)


class ElementDeleteView(DeleteView):
    model = Element
    template_name = 'element/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('element:list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ElementDeleteView, self).post(request, *args, **kwargs)