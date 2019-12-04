from django.contrib import admin
from .models import Profile, Follow

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)