from django.contrib import admin

# Register your models here.
from .models import Gifts, Wedding


class GiftsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gifts, GiftsAdmin)


class WeddingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wedding, WeddingAdmin)
