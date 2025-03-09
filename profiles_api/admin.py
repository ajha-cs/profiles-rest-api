from django.contrib import admin

from profiles_api import models

# Register your models here.
# Make it available to the django admin interface
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
