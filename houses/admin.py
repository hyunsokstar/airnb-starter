from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "address"]
    list_filter = ["pets_allowed"]
    search_fields= ["address"]
