from django.urls import path
from . import views


app_name = 'equipment'
urlpatterns = [
    path('', views.equipment_list, name='list'),
    #path('<int:pk>/', views.equipment_detail, name='detail'),
    #path('add/', views.EquipmentCreateView.as_view(), name='add'),
    #path('update/<int:pk>/', views.EquipmentUpdateView.as_view(), name='update'),
    #path('delete/<int:pk>/', views.EquipmentDeleteView.as_view(), name='delete'),
    #path('duplicate/<int:pk>/', views.equipment_duplicate, name='duplicate'),
    #path('history/', views.equipment_history_list, name='history'),
    
]