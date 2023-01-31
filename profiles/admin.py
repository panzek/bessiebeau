from django.contrib import admin

from .models import UserProfile, WishList

admin.site.register(UserProfile)
admin.site.register(WishList)
