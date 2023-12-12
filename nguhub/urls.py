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

    path('employee/', include('employee.urls', namespace='employee')),
    path('equipment/', include('equipment.urls', namespace='equipment')),

    # Довідники
     ##Location
    path('directory/location/', views.directory_location_list, name='directory_location_list'),
    path('directory/location/add/', views.LocationCreateView.as_view(), name='directory_location_add'),
    path('directory/location/update/<int:pk>/', views.LocationUpdateView.as_view(), name='directory_location_update'),
    path('directory/location/delete/<int:pk>/', views.LocationDeleteView.as_view(), name='directory_location_delete'),
     ##Placement
    path('directory/placement/', views.directory_placement_list, name='directory_placement_list'),
    path('directory/placement/add/', views.PlacementCreateView.as_view(), name='directory_placement_add'),
    path('directory/placement/update/<int:pk>/', views.PlacementUpdateView.as_view(), name='directory_placement_update'),
    path('directory/placement/delete/<int:pk>/', views.PlacementDeleteView.as_view(), name='directory_placement_delete'),
    ##ActionPost
    path('directory/actionpost/', views.directory_actionpost_list, name='directory_actionpost_list'),
    path('directory/actionpost/add/', views.ActionPostCreateView.as_view(), name='directory_actionpost_add'),
    path('directory/actionpost/update/<int:pk>/', views.ActionPostUpdateView.as_view(), name='directory_actionpost_update'),
    path('directory/actionpost/delete/<int:pk>/', views.ActionPostDeleteView.as_view(), name='directory_actionpost_delete'),
    ##EquipmentCategory
    path('directory/equipmentcategory/', views.directory_equipmentcategory_list, name='directory_equipmentcategory_list'),
    path('directory/equipmentcategory/add/', views.EquipmentCategoryCreateView.as_view(), name='directory_equipmentcategory_add'),
    path('directory/equipmentcategory/update/<int:pk>/', views.EquipmentCategoryUpdateView.as_view(), name='directory_equipmentcategory_update'),
    path('directory/equipmentcategory/delete/<int:pk>/', views.EquipmentCategoryDeleteView.as_view(), name='directory_equipmentcategory_delete'),
    ##EquipmentStatuses
    path('directory/equipmentstatus/', views.directory_equipmentstatus_list, name='directory_equipmentstatus_list'),
    path('directory/equipmentstatus/add/', views.EquipmentStatusCreateView.as_view(), name='directory_equipmentstatus_add'),
    path('directory/equipmentstatus/update/<int:pk>/', views.EquipmentStatusUpdateView.as_view(), name='directory_equipmentstatus_update'),
    path('directory/equipmentstatus/delete/<int:pk>/', views.EquipmentStatusDeleteView.as_view(), name='directory_equipmentstatus_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()