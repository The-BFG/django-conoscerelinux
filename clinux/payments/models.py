from django.db import models
from django.core.validators import MinValueValidator

class Payment(models.Model):
    product_id = models.PositiveIntegerField()  # Reference to the product ID
    amount = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])  # Adjust for currency
    currency = models.CharField(max_length=3)  # Currency code (e.g., USD, EUR)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True)  # Optional: Store Stripe payment intent ID

    def __str__(self):
        return f"Payment for Product {self.product_id} on {self.created_at}"
