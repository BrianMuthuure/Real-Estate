from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'uuid', 'user', 'gender', 'phone_number', 'country', 'city']
    list_filter = ['gender', 'country', 'city']
    list_display_links = ['id', 'uuid', 'user']


admin.site.register(Profile, ProfileAdmin)
