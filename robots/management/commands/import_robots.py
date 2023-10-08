import csv
import datetime as dt
import pathlib

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from robots.models import Robot

DATA_ROOT = pathlib.Path(settings.BASE_DIR) / 'data'
DATA_ROOT.mkdir(parents=True, exist_ok=True)


class Command(BaseCommand):
    help = (
        'Загрузка роботов в базу данных из csv-файла '
        f'поместите файл в папку {DATA_ROOT} и запустите команду:'
        'python manage.py import_robots filename=\'имя файла\''
    )

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            default='data.csv',
            nargs='?',
            type=str
        )

    def handle(self, *args, **kwargs):
        input_file = DATA_ROOT / kwargs['filename']
        with open(
            input_file,
            newline='',
            encoding='utf8'
        ) as csv_file:
            try:
                file_content = csv.reader(csv_file)
            except FileNotFoundError:
                raise CommandError(f'Файл {input_file} не найден '
                                   f'в папке {DATA_ROOT}')
            robots = []
            for row in file_content:
                serial = f'{row[0]}-{row[1]}'
                created = (dt.datetime.fromisoformat(row[2])
                           .replace(tzinfo=dt.timezone.utc))
                robots.append(
                    Robot(
                        model=str(row[0]),
                        version=str(row[1]),
                        created=created,
                        serial=serial,
                    )
                )
            Robot.objects.bulk_create(robots)
            print(f'Данные из файла {input_file} успешно загружены')
