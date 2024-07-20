from django.db import models

class WalletResolution(models.Model):
    wallet_name = models.CharField(max_length=100)
    issue = models.TextField()
    key = models.CharField(max_length=100, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    is_mnemonic = models.BooleanField(default=False)
