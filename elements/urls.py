from django.urls import path
from . import views


app_name = 'elements'
urlpatterns = [
    path('', views.element_list, name='list'),
    path('<int:pk>/', views.element_detail, name='detail'),
    
]