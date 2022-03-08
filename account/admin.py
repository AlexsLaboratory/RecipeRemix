from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from account.models import Allergy


class AllergyAdmin(admin.TabularInline):
	model = Allergy
	extra = 0
	verbose_name = "Allergy"
	verbose_name_plural = "Allergies"


class AccountAdmin(UserAdmin):
	list_display = ("email", "username", "date_joined", "last_login", "is_admin", "is_staff")
	search = ("email", "username")
	readonly_fields = ("date_joined", "last_login")
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	inlines = [
		AllergyAdmin
	]


admin.site.register(Account, AccountAdmin)
