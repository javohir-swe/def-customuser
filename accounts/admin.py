from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "is_staff",
        "is_active",
        "id",
    ]
    list_filter = ["is_staff", "is_active"]
