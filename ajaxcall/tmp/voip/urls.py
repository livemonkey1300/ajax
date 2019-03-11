from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'voip'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_voip_QUOTE', views.create_voip_QUOTE, name='create_voip_QUOTE'),
    path('edit_voip_QUOTE/<int:pk>', views.edit_voip_QUOTE, name='edit_voip_QUOTE'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:field>', views.ajax_call, name='call'),
]