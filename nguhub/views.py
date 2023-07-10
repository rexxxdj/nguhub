from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.conf import settings # import the settings file
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .forms import SignInForm

from .models import Location, Placement
from .forms import LocationCreateForm, LocationUpdateForm, PlacementCreateForm, PlacementUpdateForm

from employee.models import ActionPost, Employee, MonthJournal
from employee.forms import ActionPostCreateForm, ActionPostUpdateForm


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
                    return redirect('directory_location_list')
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


#Довідники
@login_required(login_url="/")
def directory_location_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/location_list.html'
    locations = Location.objects.all()

    sort_dict = (
        {'id':1, 'key':'address','value':'Адреса'},
        {'id':2, 'key':'name','value':'Назва'},
        )
    sort_field = request.GET.get('sort', 'address')
    sort_order = request.GET.get('order', 'asc')

    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    locations = locations.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'locations': locations,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order
    }
    return render(request, template, context)


class LocationCreateView(CreateView):
    model = Location
    template_name = 'directory/location_add.html'
    form_class = LocationCreateForm

    def get_context_data(self, **kwargs):
        context = super(LocationCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(LocationCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_location_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_location_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class LocationUpdateView(UpdateView):
    model = Location
    template_name = 'directory/location_update.html'
    form_class = LocationUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(LocationUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        employeeLocation = self.get_object()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(Location.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(LocationUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_location_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_location_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'directory/location_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_location_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(LocationDeleteView, self).post(request, *args, **kwargs)

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
def directory_placement_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/placement_list.html'
    placements = Placement.objects.all()

    sort_dict = (
        {'id':1, 'key':'location','value':'Локація'},
        {'id':2, 'key':'name','value':'Назва'},
        )
    sort_field = request.GET.get('sort', 'location')
    sort_order = request.GET.get('order', 'asc')

    ordering = (sort_field, '-' + sort_field)[sort_order == 'desc']
    placements = placements.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'placements': placements,
        'sort_dict':sort_dict,
        'sort_field': sort_field,
        'sort_order': sort_order
    }
    return render(request, template, context)


class PlacementCreateView(CreateView):
    model = Placement
    template_name = 'directory/placement_add.html'
    form_class = PlacementCreateForm

    def get_context_data(self, **kwargs):
        context = super(PlacementCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(PlacementCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_placement_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_placement_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class PlacementUpdateView(UpdateView):
    model = Placement
    template_name = 'directory/placement_update.html'
    form_class = PlacementUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(PlacementUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        employeeLocation = self.get_object()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(Location.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(PlacementUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_placement_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_placement_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class PlacementDeleteView(DeleteView):
    model = Placement
    template_name = 'directory/placement_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_placement_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(PlacementDeleteView, self).post(request, *args, **kwargs)

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
def directory_actionpost_list(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    template = 'directory/actionpost_list.html'
    actionposts = ActionPost.objects.all()

    sort_order = request.GET.get('order', 'asc')

    ordering = ('name', '-' + 'name')[sort_order == 'desc']
    actionposts = actionposts.order_by(ordering)
    
    # Передати дані в шаблон
    context = {
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME,
        'actionposts': actionposts,
        'sort_order': sort_order
    }
    return render(request, template, context)


class ActionPostCreateView(CreateView):
    model = ActionPost
    template_name = 'directory/actionpost_add.html'
    form_class = ActionPostCreateForm

    def get_context_data(self, **kwargs):
        context = super(ActionPostCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if self.request.POST.get('_save'):
            messages.success(self.request, 'Дані було успішно збережено.')
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на створення')
        return super(ActionPostCreateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_actionpost_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_actionpost_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class ActionPostUpdateView(UpdateView):
    model = ActionPost
    template_name = 'directory/actionpost_update.html'
    form_class = ActionPostUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(ActionPostUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        employeeLocation = self.get_object()
        if self.request.POST.get('_save'):
            messages.success(self.request, '\"{}\" було успішно змінено.'.format(ActionPost.name))
        if self.request.POST.get('_dismiss'):
            messages.success(self.request, 'Ви відмінили запит на зміну')
        return super(ActionPostUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('directory_actionpost_list')
        if self.request.POST.get('_dismiss'):
            return reverse_lazy('directory_actionpost_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class ActionPostDeleteView(DeleteView):
    model = ActionPost
    template_name = 'directory/actionpost_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('directory_actionpost_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ActionPostDeleteView, self).post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("signin")


class JournalView(TemplateView):
    template_name = 'other/calendar.html'

    def get_context_data(self, **kwargs):
        context = super(JournalView, self).get_context_data(**kwargs)
        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()
        else:
            today = datetime.today()
            month = date(today.year, today.month, 1)

        next_month = month + relativedelta(months=1)
        prev_month = month - relativedelta(months=1)
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')
        context['cur_month'] = month.strftime('%Y-%m-%d')
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear, mmonth)[1]
        context['month_header'] = [{'day': d,'verbose': day_abbr[weekday(myear, mmonth, d)][:2]} for d in range(1, number_of_days+1)]

        context['actionposts'] = ActionPost.objects.order_by('name')
        update_url = reverse('calendar')  
        employees020 = []
        emp020 = Employee.objects.filter(is_operator=True,actionPost__name__contains='020').order_by('lastname')

        for e in emp020:
            try:
                journal = MonthJournal.objects.get(employee=employee, actionpost='БП-020' , date=month)
            except Exception:
                journal = None

            days = []
            for day in range(1, number_of_days+1):
                days.append({
                    'day': day,
                    'present': journal and getattr(journal, 'present_day%d' %day, False) or False,
                    'date': date(myear, mmonth, day).strftime('%Y-%m-%d'),
                    })
            employees020.append({
                'fullname': e.fullname(),
                'shortname': e.shortname(),
                'rank': e.rank,
                'position': e.shortposition(),
                'id': e.id,
                'days': days,
                'update_url': update_url,
                })

        context['employees020'] = employees020

        employees220 = []
        emp220 = Employee.objects.filter(is_operator=True,actionPost__name__contains='220').order_by('lastname')

        for e in emp220:
            try:
                journal = MonthJournal.objects.get(employee=employee, actionpost='БП-220' , date=month)
            except Exception:
                journal = None

            days = []
            for day in range(1, number_of_days+1):
                days.append({
                    'day': day,
                    'present': journal and getattr(journal, 'present_day%d' %day, False) or False,
                    'date': date(myear, mmonth, day).strftime('%Y-%m-%d'),
                    })
            employees220.append({
                'fullname': e.fullname(),
                'shortname': e.shortname(),
                'rank': e.rank,
                'position': e.shortposition(),
                'id': e.id,
                'days': days,
                'update_url': update_url,
                })

        context['employees220'] = employees220

              

        return context