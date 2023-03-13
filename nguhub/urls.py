from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='signin'),
    path('logout/', views.user_logout, name='logout'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('equipment/', include('equipment.urls', namespace='equipment')),
    path('element/', include('elements.urls', namespace='element')),
    path('employee/', include('employees.urls', namespace='employee')),
    # Довідники
     ##Employee Location
    path('directory/employee/location/add/', views.EmployeeLocationCreateView.as_view(), name='directory_employee_location_add'),
    path('directory/employee/location/update/<int:pk>/', views.EmployeeLocationUpdateView.as_view(), name='directory_employee_location_update'),
    path('directory/employee/location/delete/<int:pk>/', views.EmployeeLocationDeleteView.as_view(), name='directory_employee_location_delete'),
    path('directory/employee/location/', views.directory_employee_location_list, name='directory_employee_location_list'),
      ##Equipment Category
    path('directory/equipment/category/add/', views.EquipmentCategoryCreateView.as_view(), name='directory_equipment_category_add'),
    path('directory/equipment/category/update/<int:pk>/', views.EquipmentCategoryUpdateView.as_view(), name='directory_equipment_category_update'),
    path('directory/equipment/category/delete/<int:pk>/', views.EquipmentCategoryDeleteView.as_view(), name='directory_equipment_category_delete'),
    path('directory/equipment/category/', views.directory_equipment_category_list, name='directory_equipment_category_list'),
      ##Equipment Status
    path('directory/equipment/status/add/', views.EquipmentStatusCreateView.as_view(), name='directory_equipment_status_add'),
    path('directory/equipment/status/update/<int:pk>/', views.EquipmentStatusUpdateView.as_view(), name='directory_equipment_status_update'),
    path('directory/equipment/status/delete/<int:pk>/', views.EquipmentStatusDeleteView.as_view(), name='directory_equipment_status_delete'),
    path('directory/equipment/status/', views.directory_equipment_status_list, name='directory_equipment_status_list'),
      ##Element Category
    path('directory/element/category/add/', views.ElementCategoryCreateView.as_view(), name='directory_element_category_add'),
    path('directory/element/category/update/<int:pk>/', views.ElementCategoryUpdateView.as_view(), name='directory_element_category_update'),
    path('directory/element/category/delete/<int:pk>/', views.ElementCategoryDeleteView.as_view(), name='directory_element_category_delete'),
    path('directory/element/category/', views.directory_element_category_list, name='directory_element_category_list'),
      ##Element Status
    path('directory/element/status/add/', views.ElementStatusCreateView.as_view(), name='directory_element_status_add'),
    path('directory/element/status/update/<int:pk>/', views.ElementStatusUpdateView.as_view(), name='directory_element_status_update'),
    path('directory/element/status/delete/<int:pk>/', views.ElementStatusDeleteView.as_view(), name='directory_element_status_delete'),
    path('directory/element/status/', views.directory_element_status_list, name='directory_element_status_list'),
      ##Other Locations
    path('directory/other/location/add/', views.OtherLocationCreateView.as_view(), name='directory_other_location_add'),
    path('directory/other/location/update/<int:pk>/', views.OtherLocationUpdateView.as_view(), name='directory_other_location_update'),
    path('directory/eother/location/delete/<int:pk>/', views.OtherLocationDeleteView.as_view(), name='directory_other_location_delete'),
    path('directory/other/location/', views.directory_other_location_list, name='directory_other_location_list'),
      ##Other CurrentLocations
    path('directory/other/currentlocation/add/', views.OtherCurrentLocationCreateView.as_view(), name='directory_other_currentlocation_add'),
    path('directory/other/currentlocation/<int:pk>/', views.OtherCurrentLocationUpdateView.as_view(), name='directory_other_currentlocation_update'),
    path('directory/other/currentlocation/delete/<int:pk>/', views.OtherCurrentLocationDeleteView.as_view(), name='directory_other_currentlocation_delete'),
    path('directory/other/currentlocation/', views.directory_other_currentlocation_list, name='directory_other_currentlocation_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()