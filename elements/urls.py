from django.urls import path
from . import views


app_name = 'elements'
urlpatterns = [
    path('', views.element_list, name='list'),
    path('<int:pk>/', views.element_detail, name='detail'),
    path('add/', views.ElementCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.ElementUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ElementDeleteView.as_view(), name='delete'),
    path('history/', views.element_history_list, name='history'),
    
]