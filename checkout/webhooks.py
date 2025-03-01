from django.http import HttpResponse
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt  # Webhooks should be exempt from CSRF protection
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature", "")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Process event
    if event["type"] == "checkout.session.completed":
        print("Payment Successful!")

    return HttpResponse(status=200)
