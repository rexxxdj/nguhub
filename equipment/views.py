from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Equipment


def equipment_list(request):
    equipments = Equipment.objects.all()
    order_by = request.GET.get('order_by',' ')

    if order_by in ('name','category__name','employee__fullname', 'status__name'):
        equipments = equipments.order_by(order_by)
    if request.GET.get('reverse', '') == '1':
        equipments = equipments.reverse()

    for i in equipments:
        print(i)
    return render(request, 'equipment_list.html',{'equipments': equipments})


def equipment_add(request):
    return HttpResponse('<h1>Equipment Add Form</h1>')

def equipment_edit(request, sid):
    return HttpResponse('<h1>Edit Equipment %s</h1>' % sid)

def equipment_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)