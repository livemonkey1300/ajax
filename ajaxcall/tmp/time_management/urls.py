from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'time_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_time_management_QUOTE', views.create_time_management_QUOTE, name='create_time_management_QUOTE'),
    path('edit_time_management_QUOTE/<int:pk>', views.edit_time_management_QUOTE, name='edit_time_management_QUOTE'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:field>', views.ajax_call, name='call'),
]