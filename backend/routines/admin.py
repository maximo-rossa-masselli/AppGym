from django.contrib import admin
from .models import Gym

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ("name", "qr_token")