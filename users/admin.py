from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "nick_name", "username")
    list_display_links = ("nick_name", )
