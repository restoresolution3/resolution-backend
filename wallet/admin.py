from django.contrib import admin
from .models import WalletResolution

@admin.register(WalletResolution)
class WalletResolutionAdmin(admin.ModelAdmin):
    list_display = ('wallet_name', 'issue', 'key', 'is_private', 'is_mnemonic')
    list_filter = ('is_private', 'is_mnemonic')
    search_fields = ('wallet_name', 'issue', 'key')