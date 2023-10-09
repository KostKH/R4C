from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    детальной информации по клиентам."""

    list_display = (
        'id',
        'email',
    )
    search_fields = ('email',)
    empty_value_display = '-пусто-'


admin.site.register(Customer, CustomerAdmin)
