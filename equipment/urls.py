from django.urls import path
from . import views


app_name = 'equipment'
urlpatterns = [
    path('', views.equipment_list, name='equipment'),
    #path(r'^equipment/add/$', views.equipment_add,name='equipment_add'),
    #path(r'^equipment/(?P<sid>\d+)/edit/$',views.equipment_edit,name='equipment_edit'),
    #path(r'^equipment/(?P<sid>\d+)/delete/$',views.equipment_delete,name='equipment_delete'),
    
]