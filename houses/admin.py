from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display=["name", "price", "address", "description"]
    list_filter = ["pets_allowed"]
