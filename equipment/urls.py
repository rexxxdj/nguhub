from django.urls import path
from . import views


app_name = 'equipment'
urlpatterns = [
    path('', views.equipment_list, name='list'),
    path('<int:pk>/', views.equipment_detail, name='detail'),
    path('add/', views.equipment_add, name='add'),
    path('update/<int:pk>/', views.equipment_update, name='update'),
    path('delete/<int:pk>/', views.EquipmentDeleteView.as_view(), name='delete'),
    #path(r'^equipment/(?P<sid>\d+)/edit/$',views.equipment_edit,name='equipment_edit'),
    #path(r'^equipment/(?P<sid>\d+)/delete/$',views.equipment_delete,name='equipment_delete'),
    
]