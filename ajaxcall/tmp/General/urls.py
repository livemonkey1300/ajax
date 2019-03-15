from django.urls import path
from django.conf.urls import url

from . import views
from . import accounts

app_name = 'General'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_voip', views.create_voip, name='create_voip'),
    path('edit_voip/<int:pk>', views.edit_voip, name='edit_voip'),
    path('call', views.ajax_call, name='call'),
    path('call/<slug:form_name>/', views.ajax_call, name='call'),
    path('call/<slug:form_name>/<slug:field>', views.ajax_call, name='call'),
    path('login/', accounts.login, name='login'),
    path('signup/', accounts.signup, name='signup'),
    path('home/', accounts.home, name='home'),
]