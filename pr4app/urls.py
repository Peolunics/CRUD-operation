from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('ADD_URL',views.add),
    path('DISPLAY_URL',views.display),
    path('DELETE_URL',views.delete),
    path('UPDATE_URL',views.update),
]