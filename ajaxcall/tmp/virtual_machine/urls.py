from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'virtual_machine'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_applications', views.add_applications, name='add_applications'),
    path('edit_applications/<int:id>', views.add_applications, name='edit_applications'),
    path('add_fully_managed', views.add_fully_managed, name='add_fully_managed'),
    path('edit_fully_managed/<int:id>', views.add_fully_managed, name='edit_fully_managed'),
    path('add_virtual_machine', views.add_virtual_machine, name='add_virtual_machine'),
    path('edit_virtual_machine/<int:id>', views.add_virtual_machine, name='edit_virtual_machine'),
    path('<slug:name>/submit', views.submit_ctl, name='submitctl'),
    path('<slug:name>/submit/<int:id>', views.submit_ctl, name='submitctl'),
]