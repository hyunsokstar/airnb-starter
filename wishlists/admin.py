from django.contrib import admin
from .models import WishList

# Register your models here.


@admin.register(WishList)
class WishlistAdmin(admin.ModelAdmin):
    pass


