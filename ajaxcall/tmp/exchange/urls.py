from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'exchange'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_exchange_QUOTE', views.create_exchange_QUOTE, name='create_exchange_QUOTE'),
    path('edit_exchange_QUOTE/<int:pk>', views.edit_exchange_QUOTE, name='edit_exchange_QUOTE'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:field>', views.ajax_call, name='call'),
]