from django.contrib import admin
from .models import UserProfile, UserChallenges

class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('challenges',)
    list_filter = ["gender", ]
    search_fields = ["user__username"]

admin.site.register(UserProfile, UserProfileAdmin)


class UserChallengesAdmin(admin.ModelAdmin):
    search_fields = ["user__username"]

admin.site.register(UserChallenges, UserChallengesAdmin)
