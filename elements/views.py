from django.conf import settings # import the settings file
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, QueryDict
from urllib.parse import urlencode
from django.views.generic import ListView
from .models import Element, Status, Category


def element_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'element_list.html'
    elements = Element.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
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
    print(ordering)
    elements = elements.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'elements': elements,
        'categories': categories,
        'statuses': statuses,
        'selected_categories':category_filters,
        'selected_statuses':status_filters,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order
    }
    return render(request, template, context)


def element_detail(request, pk):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'element_detail.html'
    element = get_object_or_404(Element, id=pk,)

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'element': element
    }
    return render(request, template, context)

def element_add(request):
    return HttpResponse('<h1>Element Add Form</h1>')

def element_edit(request, sid):
    return HttpResponse('<h1>Edit Element %s</h1>' % sid)

def element_delete(request, sid):
    return HttpResponse('<h1>Delete Element %s</h1>' % sid)