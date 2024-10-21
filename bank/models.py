# bank/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    account_id = models.CharField(max_length=20)
    card_id = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Добавьте это поле

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='bank_user_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='bank_user_permissions_set',
        blank=True
    )

    def __str__(self):
        return self.username

class BankCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_cards')
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry_date = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Добавлено поле balance

    def __str__(self):
        return f"Card ending with {self.card_number[-4:]}"

class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Transaction of {self.amount:.2f} from {self.sender} to {self.receiver} on {self.timestamp}"
