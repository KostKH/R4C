from django.test import TestCase

from robots.models import Robot
from robots.utils import get_robot_model


class RobotUtilsTests(TestCase):

    def test_get_robot_model_returns_correct_model(self):
        """Функция `get_robot_model` возвращает корректную модель."""
        model = get_robot_model()
        self.assertEqual(model, Robot)
