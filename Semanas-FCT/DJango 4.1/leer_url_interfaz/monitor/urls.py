from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check_changes, name='check'),
    path('done/', views.mark_all_checked, name='done'),
    path('reset/', views.reset_status, name='reset'),
]
