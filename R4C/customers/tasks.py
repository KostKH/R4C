from django.core.mail import send_mail

from R4C.celery import app


@app.task
def notify_customer(email, model, version):
    """Отправка email покупателю о поступлении робота, на который
    покупатель оставлял заказ."""
    subject = f'R4С: поступил робот {model}-{version}!'
    message = (
        'Добрый день!\n'
        f'Недавно вы интересовались нашим роботом '
        f'модели {model}, версии {version}.\n'
        'Этот робот теперь в наличии. Если вам подходит этот вариант - '
        'пожалуйста, свяжитесь с нами.\n'
        'С уважением,\n'
        'Ваш R4C!\n'
    )
    return send_mail(subject, message, 'client_service@R4C.com', [email])
