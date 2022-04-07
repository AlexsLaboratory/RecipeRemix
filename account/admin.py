from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from account.models import Allergy
from account.models import pantryItem


class AllergyAdmin(admin.TabularInline):
	model = Allergy
	extra = 0
	verbose_name = "Allergy"
	verbose_name_plural = "Allergies"

class pantryItemAdmin(admin.TabularInline):
	model = pantryItem
	extra = 0
	verbose_name = "Pantry"
	verbose_name_plural = "pantryItems"


class AccountAdmin(UserAdmin):
	list_display = ("email", "username", "date_joined", "last_login", "is_admin", "is_staff")
	search = ("email", "username")
	readonly_fields = ("date_joined", "last_login")
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	inlines = [
		AllergyAdmin,
		pantryItemAdmin
	]


admin.site.register(Account, AccountAdmin)
