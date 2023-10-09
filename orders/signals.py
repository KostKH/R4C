from customers.tasks import notify_customer
from orders.utils import get_order_model
from robots.utils import get_robot_model


def allocate_order(sender, instance, **kwargs):
    """Функция получает сигнал о поступлении заказа
    и аллоцирует на него свободного (неаллоцированного)
    робота. Если нечего аллоцировать - функция оставляет
    поле allocation в заказе пустым."""
    robot_model = get_robot_model()
    if instance.allocation:
        return
    robot = (robot_model.objects
             .filter(serial=instance.robot_serial, order__isnull=True)
             .first())
    instance.allocation = robot or None


def allocate_notificate(sender, instance, **kwargs):
    """Функция получает сигнал о поступлении нового робота
    и проверяет, есть ли заказы на этого робота без аллокации.
    Если есть - функция аллоцирует робота на заказ и отправляет
    email автору заказа о поступлении робота. Email отправляется
    через Celery."""
    order_model = get_order_model()
    order = (order_model.objects
             .filter(robot_serial=instance.serial, allocation__isnull=True)
             .first())
    if not order:
        return
    order.allocation = instance
    order.save()
    notify_customer.delay(
        order.customer.email,
        instance.model,
        instance.version
    )
