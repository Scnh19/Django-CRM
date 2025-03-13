from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    #record below
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    #inventory below
    path('inventory/', views.inventory, name='inventory'),
    path('record_inventory/<int:pk>', views.customer_inventory, name='record_inventory'),
    path('delete_inventory/<int:pk>', views.delete_inventory, name='delete_inventory'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('update_inventory/<int:pk>', views.update_inventory, name='update_inventory'),
]