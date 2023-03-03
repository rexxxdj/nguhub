from django.conf import settings # import the settings file
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Element, Status, Category
from .forms import ElementCreateForm, ElementUpdateForm
from equipment.models import Equipment


@login_required(login_url="/")
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


@login_required(login_url="/")
def element_detail(request, pk):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'element/detail.html'
    element = get_object_or_404(Element, id=pk,)

    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'element': element
    }
    return render(request, template, context)


class ElementCreateView(CreateView):
    model = Element
    template_name = 'element/add.html'
    form_class = ElementCreateForm

    def get_context_data(self, **kwargs):
        context = super(ElementCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        element = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(ElementCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('element:list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('element:list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class ElementUpdateView(UpdateView):
    model = Element
    template_name = 'element/update.html'
    form_class = ElementUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(ElementUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        element = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(element.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(ElementUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('element:list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('element:list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


@login_required(login_url="/")
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")