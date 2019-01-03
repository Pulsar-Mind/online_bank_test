from django.contrib import admin
from .models import BankAccount, UserProfile, TransactionModel

# Register your models here.
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ["account_type", "iban"]
    list_editable = ["iban"]
    list_per_page = 30

    class Meta:
        model = BankAccount


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
    list_editable = []
    list_per_page = 30

    class Meta:
        model = UserProfile

class TransactionAdmin(admin.ModelAdmin):
    list_display = ["rec_account", "sen_account", "amount", "date"]
    list_editable = []
    list_per_page = 30

    class Meta:
        model = TransactionModel


admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(TransactionModel, TransactionAdmin)

