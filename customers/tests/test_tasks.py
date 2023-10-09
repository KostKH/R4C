from django.core import mail
from django.test import TestCase

from customers.tasks import notify_customer


class CustomerTasksTests(TestCase):

    def test_notify_customer_creates_correct_email(self):
        """Функция `notify_customer` возвращает корректный email"""
        email = 'test1@test1.test1'
        model = 'T1'
        version = 'V1'

        expected_message = (
            'Добрый день!\n'
            f'Недавно вы интересовались нашим роботом '
            f'модели {model}, версии {version}.\n'
            'Этот робот теперь в наличии. Если вам подходит этот вариант - '
            'пожалуйста, свяжитесь с нами.\n'
            'С уважением,\n'
            'Ваш R4C!\n'
        )
        notify_customer(email, model, version)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'R4С: поступил робот T1-V1!')
        self.assertEqual(mail.outbox[0].to, ['test1@test1.test1'])
        self.assertEqual(mail.outbox[0].from_email, 'client_service@R4C.com')
        self.assertEqual(mail.outbox[0].body, expected_message)
