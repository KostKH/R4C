import datetime as dt

from django.forms.utils import from_current_timezone
from django.test import Client, TestCase
from django.urls import reverse

from robots.models import Robot


class RobotViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()

    def test_robots_post_correct_data_succedes(self):
        """Метод POST Эндпойнта robots записывает робота в базу
        и отдает верный ответ."""
        robot_data = {
            'model': 'R2',
            'version': 'D2',
            'created': '2022-12-31 23:59:59'
        }
        expected_serial = f"{robot_data['model']}-{robot_data['version']}"
        expected_created = from_current_timezone(
            dt.datetime.fromisoformat(robot_data['created'])
        )
        response = self.guest_client.post(
            reverse('new_robot'),
            data=robot_data,
            content_type='application/json',
        )
        new_robot = Robot.objects.order_by('-id')[:1].first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'status': 'created'})
        self.assertEqual(new_robot.model, robot_data['model'])
        self.assertEqual(new_robot.version, robot_data['version'])
        self.assertEqual(new_robot.serial, expected_serial)
        self.assertEqual(new_robot.created, expected_created)

    def test_robots_post_invalid_data_fails(self):
        """Метод POST Эндпойнта robots при отправке некорректных данных
        не создает робота и возвращает код 400."""
        len_robots_before = Robot.objects.count()
        incorrect_data_list = [
            {
                'model': 'R22',
                'version': 'D2',
                'created': '2022-12-31 23:59:59',
            },
            {
                'model': 'R2',
                'version': 'D22',
                'created': '2022-12-31 23:59:59',
            },
            {
                'model': 'R2',
                'version': 'D2',
                'created': 'aaa',
            },
            {
                'version': 'D2',
                'created': '2022-12-31 23:59:59',
            },
            {
                'model': 'R2',
                'created': '2022-12-31 23:59:59',
            },
            {
                'model': 'R2',
                'version': 'D2',
            },
            {},
        ]
        for invalid_data in incorrect_data_list:
            with self.subTest(data=str(invalid_data)):
                response = self.guest_client.post(
                    reverse('new_robot'),
                    data=invalid_data,
                    content_type='application/json',
                )
                len_robots_after = Robot.objects.count()
                self.assertEqual(response.status_code, 400)
                self.assertEqual(len_robots_before, len_robots_after)

    def test_robots_invalid_methods_not_allowed(self):
        """Эндпойнт robots не принимает запросы
        с неразрешенными методами."""
        methods = ['GET', 'PUT', 'PATCH', 'DELETE']
        len_robots_before = Robot.objects.count()

        for method in methods:
            with self.subTest(method=method):
                request_method = getattr(self.guest_client, method.lower())
                response = request_method(reverse('new_robot'))
                len_robots_after = Robot.objects.count()
                self.assertEqual(response.status_code, 405)
                self.assertEqual(len_robots_before, len_robots_after)
