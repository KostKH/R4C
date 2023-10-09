from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_robot_model():
    """
    Функция возвращает модель роботов. (Функция позволяет избежать
    зацикливания импортов).
    """
    try:
        return apps.get_model(settings.ROBOT_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("ROBOT_MODEL must be of the "
                                   "form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "ROBOT_MODEL refers to model '%s' that "
            "has not been installed" % settings.ROBOT_MODEL
        )
