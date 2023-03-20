from django.urls import path
from . import views


app_name = 'departmentEquipment'
urlpatterns = [
    path('', views.equipment_list, name='list'),
    path('<int:pk>/', views.equipment_detail, name='detail'),
    path('formular/<int:pk>/', views.equipment_get_formular, name='get_formular'),
    path('add/', views.EquipmentCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.EquipmentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.EquipmentDeleteView.as_view(), name='delete'),
    path('history/', views.equipment_history_list, name='history'),
    
]