from django.contrib import admin

from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    fields = ["username", "lastname", "firstname", "patronymic", "email",
              "is_superuser", "is_staff", "is_active"]


admin.site.register(Account, AccountAdmin)
