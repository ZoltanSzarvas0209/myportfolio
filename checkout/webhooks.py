import stripe
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Order  # Import your Order model if needed
import logging

# imports to set up emails
from django.core.mail import send_mail
from django.template.loader import render_to_string


# this code was set up with ChatGPT
# Set up logging for debugging
logger = logging.getLogger(__name__)


@csrf_exempt  # Exempt CSRF for webhook calls
def stripe_webhook(request):
    """Handles Stripe webhook events"""
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        logger.error("⚠️ Invalid payload: %s", e)
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error("❌ Invalid signature: %s", e)
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    # Log received event
    logger.info(f"🔔 Webhook received: {event['type']}")

    # Handling specific Stripe events
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        handle_checkout_session(session)

    elif event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        logger.info(f"✅ Payment Intent Succeeded: {payment_intent}")

    elif event["type"] == "customer.subscription.created":
        subscription = event["data"]["object"]
        logger.info(f"📄 New Subscription Created: {subscription}")

    elif event["type"] == "invoice.payment_failed":
        invoice = event["data"]["object"]
        logger.warning(f"⚠️ Invoice Payment Failed: {invoice}")

    # Add more event handlers as needed

    return HttpResponse(status=200)


def handle_checkout_session(session):
    """Process the checkout session after successful payment"""
    logger.info(f"✅ Checkout Session Completed: {session}")

    # Retrieve metadata if sent during session creation
    order_id = session.get("metadata", {}).get("order_id")

    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            order.is_paid = True
            order.save()
            logger.info(f"✅ Order {order_id} marked as paid")

            # Send confirmation email after order is marked as paid
            _send_confirmation_email(order)

        except Order.DoesNotExist:
            logger.error(f"❌ Order {order_id} not found")


def _send_confirmation_email(self, order):
    """Send the user a confirmation email"""
    cust_email = order.email
    subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
    body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
        )
