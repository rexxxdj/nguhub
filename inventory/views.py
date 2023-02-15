import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_downloadview import PathDownloadView
#from .models import Device


# Create your views here.

#class InventoryListView(ListView):
#    #model = Inventory
#    template_name = 'inventory_list.html'
#    paginate_by = 20

#    def get_queryset(self):
#        return super().get_queryset()

#    def get_context_data(self):
#        context = super(InventoryListView, self).get_context_data()
#        return context