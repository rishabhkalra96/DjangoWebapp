from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'Information', 'phone', 'website_owned', 'city')

    def Information(self, obj):
        return obj.description

    def website_owned(self, obj):
        return obj.website
    
admin.site.register(UserProfile, UserProfileAdmin)


