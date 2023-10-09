from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save

from orders.signals import allocate_notificate, allocate_order
from orders.utils import get_order_model
from robots.utils import get_robot_model


class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self):
        order_model = get_order_model()
        robot_model = get_robot_model()
        pre_save.connect(allocate_order, sender=order_model)
        post_save.connect(allocate_notificate, sender=robot_model)
