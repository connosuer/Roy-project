from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50)
    connection_type = models.CharField(max_length=50)
    auth_token_id = models.CharField(max_length=100)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    balance_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s account at {self.institution.name}"

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    trn_date = models.DateTimeField()
    trn_type = models.CharField(max_length=50)
    trn_description = models.TextField()
    trn_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.user.username}'s transaction of {self.trn_amount} on {self.trn_date}"