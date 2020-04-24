
# Create your views here.
from django.views.generic import TemplateView

from .models import Order, Driver, Farmer


class OrdersView(TemplateView):
    template_name = 'control_panel/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        context['orders'] = self.process_orders(orders)
        context['drivers'] = self.process_drivers(Driver.objects.all(), orders)

        return context

    def process_orders(self, orders):
        orders_new = []
        orders_in_progress = []
        orders_done = []
        for order in orders:
            order.pickup_address = f'{order.farmer.street} {order.farmer.house_nr} ' \
                f'{order.farmer.house_nr_extension}, {order.farmer.zipcode}'

            if order.arrival_time is None and order.driver is None:
                orders_new.append(order)
            elif order.arrival_time is None and order.driver is not None:
                orders_in_progress.append(order)
            elif order.arrival_time is not None:
                orders_done.append(order)

        return {
            'orders_new': orders_new,
            'orders_in_progress': orders_in_progress,
            'orders_done': orders_done
        }

    def process_drivers(self, drivers, orders):
        available_drivers = []
        for driver in drivers:
            found = False
            for order in orders:
                if driver == order.driver:
                    found = True
            if not found:
                available_drivers.append(driver)
        return available_drivers


class DriverView(TemplateView):
    template_name = 'control_panel/drivers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drivers'] = Driver.objects.all()


class FarmerView(TemplateView):
    template_name = 'control_panel/farmers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['farmers'] = Farmer.objects.all()
