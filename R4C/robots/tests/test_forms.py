from django.test import TestCase

from robots.forms import RobotForm


class RobotFormTests(TestCase):

    def test_correct_data_return_valid_form(self):
        """Корректные данные возвращают валидную форму"""
        robot_data = {
            'model': 'R2',
            'version': 'D2',
            'created': '2022-12-31 23:59:59'
        }
        form = RobotForm(robot_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_incorrect_data_return_invalid_form(self):
        """Ошибочные данные не проходят валидацию: возвращаются ошибки."""
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
                form = RobotForm(invalid_data)
                self.assertFalse(form.is_valid())
                self.assertTrue(form.errors)
