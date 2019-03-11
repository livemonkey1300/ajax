from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'virtual_machine'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_applications', views.create_applications, name='create_applications'),
    path('edit_applications/<int:pk>', views.edit_applications, name='edit_applications'),
    path('create_fully_managed', views.create_fully_managed, name='create_fully_managed'),
    path('edit_fully_managed/<int:pk>', views.edit_fully_managed, name='edit_fully_managed'),
    path('create_virtual_machine_QUOTE', views.create_virtual_machine_QUOTE, name='create_virtual_machine_QUOTE'),
    path('edit_virtual_machine_QUOTE/<int:pk>', views.edit_virtual_machine_QUOTE, name='edit_virtual_machine_QUOTE'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:field>', views.ajax_call, name='call'),
]
