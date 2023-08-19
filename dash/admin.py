from django.contrib import admin
from .models import UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address','user')

admin.site.register(UserProfile, UserAdmin)

from .models import UserProfile, ConfirmedUserProfile

class ConfirmedUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address','user')

admin.site.register(ConfirmedUserProfile, ConfirmedUserAdmin)
