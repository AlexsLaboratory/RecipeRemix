from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from account.models import Allergy
from account.models import Pantry


class AllergyAdmin(admin.TabularInline):
	model = Allergy
	extra = 0
	verbose_name = "Allergy"
	verbose_name_plural = "Allergies"


class PantryAdmin(admin.TabularInline):
	model = Pantry
	extra = 0
	verbose_name = "Pantry"


class AccountAdmin(UserAdmin):
	list_display = ("email", "username", "date_joined", "last_login", "is_admin", "is_staff")
	search = ("email", "username")
	readonly_fields = ("date_joined", "last_login")
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	inlines = [
		AllergyAdmin,
		PantryAdmin
	]


admin.site.register(Account, AccountAdmin)
