import stripe
from django.shortcuts import render, redirect
from events.models import Event
from django.conf import settings

def create_checkout_session(request, event_id):
    event = Event.objects.get(pk=event_id)

    # Retrieve Stripe secret key securely from environment variables
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        #ui_mode = 'embedded',
        #payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'eur',  # Adjust for your currency
                    'product_data': {
                        'name': event.title,
                        'description': event.description,
                    },
                    'unit_amount': int(event.price * 100),  # Convert to cents
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=f'http://localhost:8000/payments/success/?event_id={event_id}',
        cancel_url=f'http://localhost:8000/payments/cancel/',
    )
    return render(request, 'payments/payment.html', {'event': event, 'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY, 'session_id': session.id})

def payment_success(request):
    event_id = request.GET.get('event_id')  # Retrieve product ID from query string
    if event_id:
        # Handle successful payment (e.g., display a success message, create a payment record)
        return render(request, 'payments/payment_success.html')  # Optional: success template
    else:
        return redirect('home')  # Redirect to homepage if product ID is missing

def payment_cancel(request):
    # Handle canceled payment (e.g., display a cancellation message)
    return render(request, 'payments/payment_cancel.html')  # Optional: cancel template
