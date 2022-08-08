from django.contrib import admin
from django.contrib.admin.options import TabularInline
from rest.models import Category, Selection, Sale, Restaurant, Image


class RestaurantImageAdminInline(TabularInline):
    extra = 0
    model = Image
    max_num = 100


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['name']


@admin.register(Selection)
class SelectionModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['name']


@admin.register(Sale)
class SaleModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['name', 'time_create', 'time_update', ]


@admin.register(Restaurant)
class RestaurantModelAdmin(admin.ModelAdmin):
    inlines = (RestaurantImageAdminInline, )
    readonly_fields = ['id']
    list_display = ['name', 'phone_number_1', ]
