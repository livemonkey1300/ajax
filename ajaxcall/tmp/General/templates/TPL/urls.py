        path('create_voip', views.create_voip, name='create_voip'),
        path('edit_voip/<int:pk>', views.edit_voip, name='edit_voip'),