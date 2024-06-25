from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from accommodation.models import Accommodation
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_display = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('name', 'availability_start', 'availability_end')
    list_filter = ('availability_start', 'availability_end',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Accommodation, AccommodationAdmin)