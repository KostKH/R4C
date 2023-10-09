from django.test import TestCase

from orders.models import Order
from orders.utils import get_order_model


class OrderUtilsTests(TestCase):

    def test_get_order_model_returns_correct_model(self):
        """Функция `get_order_model` возвращает корректную модель"""
        model = get_order_model()
        self.assertEqual(model, Order)
