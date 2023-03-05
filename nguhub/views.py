import datetime
from django.conf import settings # import the settings file
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import SignInForm, EmployeeLocationCreateForm, EmployeeLocationUpdateForm
from .forms import EquipmentCategoryCreateForm, EquipmentCategoryUpdateForm, EquipmentStatusCreateForm, EquipmentStatusUpdateForm
from .forms import ElementCategoryCreateForm, ElementCategoryUpdateForm, ElementStatusCreateForm, ElementStatusUpdateForm
from employees.models import Category as employeeLocation
from equipment.models import Category as equipmentCategory, Status as equipmentStatus
from elements.models import Category as elementCategory, Status as elementStatus


def user_login(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('equipment:list')
                else:
                    return HttpResponse('Акаунт не активний')
            else:
                return HttpResponse('Невірний логін або пароль')
    else:
        form = SignInForm()

    context = {
        'form': form,
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME
    }
    return render(request, 'signin.html', context)


def user_logout(request):
    logout(request)
    url = reverse('signin')
    return HttpResponseRedirect(url)


@login_required(login_url="/")
def directory_employee_location_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/employee/location_list.html'
    employeeLocations = employeeLocation.objects.all()
    sort_dict = (
        {'id':1, 'key':'address','value':'Адреса'},
        {'id':2, 'key':'name','value':'Локація'},
        )
    sort_field = request.GET.get('sort', 'id')
    sort_order = request.GET.get('order', 'desc')

    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    employeeLocations = employeeLocations.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'employeeLocations': employeeLocations,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order
    }
    return render(request, template, context)


class EmployeeLocationCreateView(CreateView):
    model = employeeLocation
    template_name = 'directory/employee/location_add.html'
    form_class = EmployeeLocationCreateForm

    def get_context_data(self, **kwargs):
        context = super(EmployeeLocationCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        equipment = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(EmployeeLocationCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_employee_location_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_employee_location_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class EmployeeLocationUpdateView(UpdateView):
    model = employeeLocation
    template_name = 'directory/employee/location_update.html'
    form_class = EmployeeLocationUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(EmployeeLocationUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        employeeLocation = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(employeeLocation.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(EmployeeLocationUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_employee_location_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_employee_location_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class EmployeeLocationDeleteView(DeleteView):
    model = employeeLocation
    template_name = 'directory/employee/location_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_employee_location_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EmployeeLocationDeleteView, self).post(request, *args, **kwargs)

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
def directory_equipment_category_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/equipment/category_list.html'
    equipmentCategories = equipmentCategory.objects.all()

    sort_field = 'name'
    sort_order = request.GET.get('order', 'desc')

    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    equipmentCategories = equipmentCategories.order_by(ordering)
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'equipmentCategories': equipmentCategories,
        'sort_order': sort_order
    }
    return render(request, template, context)


class EquipmentCategoryCreateView(CreateView):
    model = equipmentCategory
    template_name = 'directory/equipment/category_add.html'
    form_class = EquipmentCategoryCreateForm

    def get_context_data(self, **kwargs):
        context = super(EquipmentCategoryCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        equipmentCategory = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(EquipmentCategoryCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_equipment_category_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_equipment_category_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class EquipmentCategoryUpdateView(UpdateView):
    model = equipmentCategory
    template_name = 'directory/equipment/category_update.html'
    form_class = EquipmentCategoryUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(EquipmentCategoryUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        equipmentCategory = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(equipmentCategory.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(EquipmentCategoryUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_equipment_category_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_equipment_category_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class EquipmentCategoryDeleteView(DeleteView):
    model = equipmentCategory
    template_name = 'directory/equipment/category_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_equipment_category_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EquipmentCategoryDeleteView, self).post(request, *args, **kwargs)

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
def directory_equipment_status_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/equipment/status_list.html'
    equipmentStatuses = equipmentStatus.objects.all()

    sort_field = 'name'
    sort_order = request.GET.get('order', 'desc')

    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    equipmentStatuses = equipmentStatuses.order_by(ordering)
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'equipmentStatuses': equipmentStatuses,
        'sort_order': sort_order
    }
    return render(request, template, context)


class EquipmentStatusCreateView(CreateView):
    model = equipmentStatus
    template_name = 'directory/equipment/status_add.html'
    form_class = EquipmentStatusCreateForm

    def get_context_data(self, **kwargs):
        context = super(EquipmentStatusCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        equipmentStatus = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(EquipmentStatusCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_equipment_status_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_equipment_status_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class EquipmentStatusUpdateView(UpdateView):
    model = equipmentStatus
    template_name = 'directory/equipment/status_update.html'
    form_class = EquipmentStatusUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(EquipmentStatusUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        equipmentStatus = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(equipmentStatus.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(EquipmentStatusUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_equipment_status_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_equipment_status_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class EquipmentStatusDeleteView(DeleteView):
    model = equipmentStatus
    template_name = 'directory/equipment/status_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_equipment_status_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(EquipmentStatusDeleteView, self).post(request, *args, **kwargs)

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
def directory_element_category_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/element/category_list.html'
    elementCategories = elementCategory.objects.all()

    sort_field = 'name'
    sort_order = request.GET.get('order', 'desc')

    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    elementCategories = elementCategories.order_by(ordering)
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'elementCategories': elementCategories,
        'sort_order': sort_order
    }
    return render(request, template, context)


class ElementCategoryCreateView(CreateView):
    model = elementCategory
    template_name = 'directory/element/category_add.html'
    form_class = ElementCategoryCreateForm

    def get_context_data(self, **kwargs):
        context = super(ElementCategoryCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        equipmentCategory = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(ElementCategoryCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_element_category_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_element_category_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class ElementCategoryUpdateView(UpdateView):
    model = elementCategory
    template_name = 'directory/element/category_update.html'
    form_class = ElementCategoryUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(ElementCategoryUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        elementCategory = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(elementCategory.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(ElementCategoryUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_element_category_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_element_category_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class ElementCategoryDeleteView(DeleteView):
    model = elementCategory
    template_name = 'directory/element/category_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_element_category_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ElementCategoryDeleteView, self).post(request, *args, **kwargs)

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
def directory_element_status_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/element/status_list.html'
    elementStatuses = elementStatus.objects.all()

    sort_field = 'name'
    sort_order = request.GET.get('order', 'desc')

    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    elementStatuses = elementStatuses.order_by(ordering)
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'elementStatuses': elementStatuses,
        'sort_order': sort_order
    }
    return render(request, template, context)


class ElementStatusCreateView(CreateView):
    model = elementStatus
    template_name = 'directory/element/status_add.html'
    form_class = ElementStatusCreateForm

    def get_context_data(self, **kwargs):
        context = super(ElementStatusCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        equipmentStatus = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(ElementStatusCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_element_status_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_element_status_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class ElementStatusUpdateView(UpdateView):
    model = elementStatus
    template_name = 'directory/element/status_update.html'
    form_class = ElementStatusUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(ElementStatusUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        elementStatus = form.save()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(elementStatus.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(ElementStatusUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_element_status_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_element_status_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class ElementStatusDeleteView(DeleteView):
    model = elementStatus
    template_name = 'directory/element/status_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_element_status_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ElementStatusDeleteView, self).post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")