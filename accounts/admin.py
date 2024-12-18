from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "date_joined",
        "is_staff",
        "is_active",
        "id",
    ]
    list_filter = ["is_staff", "is_active"]
