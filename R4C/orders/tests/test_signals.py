import datetime as dt

from django.test import Client, TestCase

from customers.models import Customer
from orders.models import Order
from robots.models import Robot


class OrderSignalTests(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.robot = Robot.objects.create(
            model='O1',
            version='Q1',
            created=dt.datetime.now().replace(tzinfo=dt.timezone.utc),
            serial='O1-Q1',
        )
        self.customer = Customer.objects.create(email='test11@test11.test11')
        self.order = Order.objects.create(
            customer=self.customer,
            robot_serial='N1-M1'
        )

    def test_allocate_order_allocates_correctly(self):
        """Функция allocate_order аллоцирует робота при его наличии."""
        order = Order.objects.create(
            customer=self.customer,
            robot_serial='O1-Q1'
        )
        self.assertEqual(order.allocation, self.robot)

    def test_allocate_order_doesnt_allocate_twice_same_robot(self):
        """Функция allocate_order не аллоцирует одного робота дважды."""
        Order.objects.create(
            customer=self.customer,
            robot_serial='O1-Q1'
        )
        order = Order.objects.create(
            customer=self.customer,
            robot_serial='O1-Q1'
        )
        self.assertIsNone(order.allocation)

    def test_allocate_notificate_allocates_when_robot_is_added(self):
        """Функция allocate_notificate аллоцирует добавленного робота,
        если есть заказ без аллокации."""
        robot = Robot.objects.create(
            model='N1',
            version='M1',
            created=dt.datetime.now().replace(tzinfo=dt.timezone.utc),
            serial='N1-M1',
        )
        self.order.refresh_from_db()
        self.assertEqual(self.order.allocation, robot)
