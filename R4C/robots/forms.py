from django.forms import ModelForm

from .models import Robot


class RobotForm(ModelForm):
    """Класс генерит форму для создания/изменения статей."""

    class Meta:
        model = Robot
        fields = [
            'model',
            'version',
            'created',
        ]
        required = {
            'model': True,
            'version': True,
            'created': True,
        }
