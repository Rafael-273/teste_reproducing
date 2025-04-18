import uuid
from django.db import models
from ._base import BaseModel


class Client(BaseModel):
    CLIENT_TYPE_CHOICES = [
        ('PF_BR', 'Individual - Brazil'),
        ('PJ_BR', 'Company - Brazil'),
        ('PF_US', 'Individual - USA'),
        ('PJ_US', 'Company - USA'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('boleto', 'Boleto Bancário'),
        ('paypal', 'PayPal'),
        ('pix', 'Pix'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPE_CHOICES)
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)

    cpf = models.CharField(max_length=14, blank=True, null=True, unique=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True, unique=True)
    ssn = models.CharField(max_length=11, blank=True, null=True, unique=True)
    ein = models.CharField(max_length=9, blank=True, null=True, unique=True)
    state_registration = models.CharField(max_length=20, blank=True, null=True)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)

    country = models.CharField(max_length=10, choices=[('BR', 'Brazil'), ('US', 'United States')])
    state = models.CharField(max_length=50)
    state_abbr = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    currency = models.CharField(max_length=3, choices=[('BRL', 'Real'), ('USD', 'Dollar')])
    preferred_payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, blank=True, null=True)

    foundation_date = models.DateField(blank=True, null=True)
    responsible_person = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
