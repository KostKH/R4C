
import csv
import datetime as dt

from django.test import TestCase

from robots.management.commands.import_robots import DATA_ROOT, Command
from robots.models import Robot


class RobotCommandTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_file = 'test_data.csv'
        cls.test_data = [
            {
                'model': 'R2',
                'version': 'D2',
                'created': '2022-12-31 23:59:59',
            },
            {
                'model': 'S5',
                'version': 'K8',
                'created': '2023-07-31 12:40:59',
            },
        ]
        with open(DATA_ROOT / cls.test_file, 'w',
                  newline='', encoding='utf-8') as csv_file:
            for item in cls.test_data:
                csv_writer = csv.DictWriter(
                    csv_file,
                    fieldnames=cls.test_data[0].keys(),)
                csv_writer.writerow(item)

    @classmethod
    def tearDownClass(cls):
        file = DATA_ROOT / cls.test_file
        file.unlink()
        super().tearDownClass()

    def test_import_command_creates_db_correct(self):
        """Команда иморта роботов создает корректные записи в БД."""
        command = Command()
        command.handle(filename=self.test_file)
        created = Robot.objects.all()
        self.assertEqual(len(created), len(self.test_data))
        for idx, robot in enumerate(self.test_data):
            expected_serial = f"{robot['model']}-{robot['version']}"
            expected_created = (dt.datetime.fromisoformat(robot['created'])
                                .replace(tzinfo=dt.timezone.utc))
            with self.subTest(robot=robot):
                self.assertEqual(created[idx].model, robot['model'])
                self.assertEqual(created[idx].version, robot['version'])
                self.assertEqual(created[idx].serial, expected_serial)
                self.assertEqual(created[idx].created, expected_created)
