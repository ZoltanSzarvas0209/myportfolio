from django.urls import path
from . import views
from .webhooks import stripe_webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success,
         name='checkout_success'),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
]
