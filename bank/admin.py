from django.contrib import admin
from .models import User, BankCard, Transaction

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'location', 'account_id', 'card_id')
    search_fields = ('username', 'phone_number', 'location')

class BankCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expiry_date')
    search_fields = ('card_number',)
    list_filter = ('user',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'amount', 'timestamp')
    search_fields = ('sender__username', 'receiver__username')
    list_filter = ('timestamp',)

admin.site.register(User, UserAdmin)
admin.site.register(BankCard, BankCardAdmin)
admin.site.register(Transaction, TransactionAdmin)
