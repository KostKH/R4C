from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    детальной информации по заказам."""

    list_display = (
        'id',
        'customer',
        'robot_serial',
        'allocation',
    )
    list_filter = ('customer', 'robot_serial',)
    empty_value_display = '-пусто-'


admin.site.register(Order, OrderAdmin)
