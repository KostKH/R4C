import datetime as dt

from django.test import Client, TestCase

from robots.models import Robot


class ReportingURLTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.test_data = [
            {
                'model': 'R2',
                'version': 'D2',
                'created': '2023-10-02 00:00:00',
            },
            {
                'model': 'R2',
                'version': 'G7',
                'created': '2023-10-08 23:59:59',
            },
        ]
        for item in cls.test_data:
            Robot.objects.create(
                model=str(item['model']),
                version=str(item['version']),
                created=(dt.datetime.fromisoformat(item['created'])
                         .replace(tzinfo=dt.timezone.utc)),
                serial=f"{item['model']}-{item['version']}",
            )

    def test_report_urls_are_available_for_guest(self):
        """GET: url из списка доступны."""
        urls_for_guest = [
            ('/', 200),
            ('/production-report/2023/40/', 200),
        ]
        for each_url, code in urls_for_guest:
            with self.subTest(each_url=each_url):
                response = self.guest_client.get(each_url)
                self.assertEqual(response.status_code, code)
