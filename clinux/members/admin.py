from django.contrib import admin

from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "first_name",
        "last_name",
        "social_id",
        "gender",
        "birth_date",
    ]
