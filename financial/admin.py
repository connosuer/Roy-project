from django.contrib import admin
from .models import Institution, Account, Transaction

admin.site.register(Institution)
admin.site.register(Account)
admin.site.register(Transaction)