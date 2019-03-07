from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'ajaxcall'
urlpatterns = [
    path('', views.index, name='index'),
    path('call/<slug:field>', views.call, name='call'),
    path('call/<slug:field>/<slug:fsub>', views.call, name='call'),
    path('call/', views.call, name='call'),
    path('create/', views.init_types, name='init_types'),
]
