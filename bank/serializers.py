from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Account, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer 
        fields = ['id', 'user', 'phone', 'email']

class AccountSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Account
        fields = ['id', 'account_number', 'account_type', 'balance', 'customer']

class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'transaction_type', 'amount', 'timestamp']