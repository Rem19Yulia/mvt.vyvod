from django.contrib import admin
from .models import Buyer, Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Отображение полей
    list_filter = ('size', 'cost')  # Фильтрация по полям
    search_fields = ('title',)  # Поиск по полю
    list_per_page = 20  # Ограничение кол-ва записей

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображение полей
    list_filter = ('balance', 'age')  # Фильтрация по полям
    search_fields = ('name',)  # Поиск по полю
    list_per_page = 30  # Ограничение кол-ва записей
    readonly_fields = ('balance',)  # Поле только для чтения
