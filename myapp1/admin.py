from django.contrib import admin
from django.db import models
from .models import Type, Item, Client, OrderItems, Description
# Register your models here.


@admin.action(description='First Name Caps')
def firstnameupper(obj):
    return obj.first_name.upper()


class ItemInline(admin.TabularInline):
    model = Item


class TypeAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline
    ]


admin.site.register(Type, TypeAdmin)
admin.site.register(Item)
admin.site.register(Client)
admin.site.register(OrderItems)
admin.site.register(Description)

