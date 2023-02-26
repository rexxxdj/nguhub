from django.urls import path
from . import views


app_name = 'employee'
urlpatterns = [
    path('', views.employee_list, name='list'),
    path('<int:pk>/', views.employee_detail, name='detail'),
    #path(r'^equipment/add/$', views.equipment_add,name='equipment_add'),
    #path(r'^equipment/(?P<sid>\d+)/edit/$',views.equipment_edit,name='equipment_edit'),
    #path(r'^equipment/(?P<sid>\d+)/delete/$',views.equipment_delete,name='equipment_delete'),
    
]