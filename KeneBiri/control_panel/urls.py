from django.urls import path

from . import views

app_name = 'control_panel'

urlpatterns = [
    path('', views.ControlPanelView.as_view(), name='index'),
]