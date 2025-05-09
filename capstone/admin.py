from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Quiz

class ProfileAdmin(UserAdmin):
    list_display = ('username', 'date_joined', 'last_login', 'points')
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ('username', 'points')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Quiz)