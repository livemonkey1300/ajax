from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'voip'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_voip', views.add_voip, name='add_voip'),
    path('edit_voip/<int:id>', views.add_voip, name='edit_voip'),
    path('<slug:name>/submit', views.submit_ctl, name='submitctl'),
    path('<slug:name>/submit/<int:id>', views.submit_ctl, name='submitctl'),
]