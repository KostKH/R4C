from django.test import Client, TestCase


class RobotURLTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()

    def test_robot_url_is_available_for_guest_post_method(self):
        """POST: Эндпойнт `robots` доступен."""
        robot_data = {
            'model': 'R2',
            'version': 'D2',
            'created': '2022-12-31 23:59:59'
        }
        response = self.guest_client.post(
            '/robots/',
            data=robot_data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)

    def test_robot_url_is_not_available_for_guest_get_method(self):
        """GET: Эндпойнт `robots` не доступен."""
        response = self.guest_client.get('/robots/')
        self.assertEqual(response.status_code, 405)
