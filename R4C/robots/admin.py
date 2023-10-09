from django.contrib import admin

from .models import Robot


class RobotAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    детальной информации по роботам."""

    list_display = (
        'id',
        'serial',
        'model',
        'version',
        'created',
    )
    list_filter = ('model', 'version', 'serial',)
    search_fields = ('serial',)
    empty_value_display = '-пусто-'


admin.site.register(Robot, RobotAdmin)
