from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=70, unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Account(models.Model):
    ACCOUNT_TYPES = [
        ('CHECKING', 'Checking')
        ('SAVING', 'Saving')
    ]    

    account_number = models.CharField(max_length=25, unique=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    customer = models.ForeignKey(Customer, related_name='accounts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} - {self.account_type}: ${self.balance}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
    ]
    
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.account}"