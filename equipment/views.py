from django.conf import settings # import the settings file
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, QueryDict
from django.views.generic import ListView
from .models import Equipment, Status, Category
from .forms import EquipmentsFilterForm


def equipment_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    equipments = Equipment.objects.all()

    #фільтр по категоріям
    if 'category' in request.GET:
        equipments = equipments.filter(category__name__in=request.GET.getlist('category'))
    #фільтр по статусу
    if 'status' in request.GET:
        equipments = equipments.filter(status__name__in=request.GET.getlist('status'))

    selected_categories = request.GET.getlist('category')
    selected_statuses = request.GET.getlist('status')

    # сортування списків
    order_by = request.GET.get('order_by',' ')
    if order_by in ('name','category__name','employee__fullname', 'status__name'):
        equipments = equipments.order_by(order_by)
    if request.GET.get('reverse', '') == '1':
        equipments = equipments.reverse()

    categories = Category.objects.all()
    statuses = Status.objects.all()

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'equipments': equipments,
        'categories': categories,
        'statuses': statuses,
        'selected_categories':selected_categories,
        'selected_statuses':selected_statuses
    }

    return render(request, 'equipment_list.html',context)

    '''selected_categories = request.GET.getlist('categories')
    equipments = Equipment.objects.all()
    if selected_categories:
        equipments = equipments.filter(category_id__in=selected_categories)
    categories = Category.objects.all()
    categories_form = EquipmentsFilterForm()
    status = Status.objects.all()
    order_by = request.GET.get('order_by',' ')
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    #if selected_categories != '[]':
    #    queryset = queryset.filter(category_id__in=selected_categories)
    #if selected_category:
    #    equipments = equipments.filter(category=selected_category)
    #if selected_status:
    #    equipments = equipments.filter(status=selected_status)

    if order_by in ('name','category__name','employee__fullname', 'status__name'):
        equipments = equipments.order_by(order_by)
    if request.GET.get('reverse', '') == '1':
        equipments = equipments.reverse()

    print(categories)

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'equipments': equipments,
        'categories': categories,
        'status': status,
        'categories_form':categories_form,
        'selected_categories': selected_categories
    }
    return render(request, 'equipment_list.html',context)'''


def equipment_add(request):
    return HttpResponse('<h1>Equipment Add Form</h1>')

def equipment_edit(request, sid):
    return HttpResponse('<h1>Edit Equipment %s</h1>' % sid)

def equipment_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)