from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_order_model():
    """
    Функция возвращает модель заказов. (Функция позволяет избежать
    зацикливания импортов).
    """
    try:
        return apps.get_model(settings.ORDER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("ORDER_MODEL must be of the "
                                   "form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "ORDER_MODEL refers to model '%s' that "
            "has not been installed" % settings.ORDER_MODEL
        )
