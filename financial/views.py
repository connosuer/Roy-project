from django.shortcuts import render
from .models import Account

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'financial/account_list.html', {'accounts': accounts})