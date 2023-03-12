from django.urls import path
from . import views


app_name = 'employee'
urlpatterns = [
    path('', views.employee_list, name='list'),
    path('<int:pk>/', views.employee_detail, name='detail'),
    path('add/', views.EmployeeCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete'),
    path('history/', views.employee_history_list, name='history'),
    
]