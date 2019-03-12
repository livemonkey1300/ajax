from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'General'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_exchange', views.create_exchange, name='create_exchange'),
    path('edit_exchange/<int:pk>', views.edit_exchange, name='edit_exchange'),
    path('create_voip', views.create_voip, name='create_voip'),
    path('edit_voip/<int:pk>', views.edit_voip, name='edit_voip'),
    path('create_virtual_machine', views.create_virtual_machine, name='create_virtual_machine'),
    path('edit_virtual_machine/<int:pk>', views.edit_virtual_machine, name='edit_virtual_machine'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:field>', views.ajax_call, name='call'),
]