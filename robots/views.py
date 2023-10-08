import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import RobotForm


@require_POST
@csrf_exempt
def new_robot(request):
    """Функция обрабатвает POST-запрос на добавление
    нового робота в базу данных."""

    try:
        robot_data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return JsonResponse({'errors': 'Incorrect JSON'}, status=400)

    form = RobotForm(robot_data)
    if form.is_valid():
        robot = form.save(commit=False)
        robot.serial = f'{robot.model}-{robot.version}'
        robot.save()
        return JsonResponse({'status': 'created'}, status=201)

    errors = {'errors': json.loads(form.errors.as_json())}
    return JsonResponse(errors, status=400)
