from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, User


# Register your models here.
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ['shopName', 'shopLocation']
    search_fields = ['shopName', ]


@admin.register(User)
class UserAdmin(OSMGeoAdmin):
    list_display = ['username', 'userLocation']
    search_fields = ['username', ]
