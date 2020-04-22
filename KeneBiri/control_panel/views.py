from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import Orders, Driver


class ControlPanelView(TemplateView):
    template_name = 'control_panel/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Orders.objects.all()
        context['drivers'] = Driver.objects.all()

        return context
