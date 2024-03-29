from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline,)
	list_display = ('username', 'realname', 'email', 'is_staff', 'is_active', 'is_superuser')

	def realname(self, obj):
		return obj.profile.realname
	realname.short_description = '姓名'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'realname')