from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'General_CMS'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_time_management', views.create_time_management, name='create_time_management'),
    path('edit_time_management/<int:pk>', views.edit_time_management, name='edit_time_management'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:form_name>/', views.ajax_call, name='call'),
    path('call/<slug:form_name>/<slug:field>', views.ajax_call, name='call'),
]