from django.urls import path
from django.conf.urls import url

from . import views
from . import accounts

app_name = 'General'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_time_management', views.create_time_management, name='create_time_management'),
    path('edit_time_management/<int:pk>', views.edit_time_management, name='edit_time_management'),
    path('create_exchange', views.create_exchange, name='create_exchange'),
    path('edit_exchange/<int:pk>', views.edit_exchange, name='edit_exchange'),
    path('create_voip', views.create_voip, name='create_voip'),
    path('edit_voip/<int:pk>', views.edit_voip, name='edit_voip'),
    path('create_virtual_machine', views.create_virtual_machine, name='create_virtual_machine'),
    path('edit_virtual_machine/<int:pk>', views.edit_virtual_machine, name='edit_virtual_machine'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:form_name>/', views.ajax_call, name='call'),
    path('call/<slug:form_name>/<slug:field>', views.ajax_call, name='call'),
    path('login/', accounts.login, name='login'),
    path('signup/', accounts.signup, name='signup'),
    path('home/', accounts.home, name='home'),
]