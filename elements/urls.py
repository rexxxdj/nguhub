from django.urls import path
from . import views


app_name = 'elements'
urlpatterns = [
    path('', views.element_list, name='list'),
    path('<int:pk>/', views.element_detail, name='detail'),
    path('add/', views.element_add, name='add'),
    path('update/<int:pk>/', views.element_update, name='update'),
    path('delete/<int:pk>/', views.ElementDeleteView.as_view(), name='delete'),
    
]