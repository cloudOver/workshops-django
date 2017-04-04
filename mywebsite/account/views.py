from django.shortcuts import render, HttpResponse
from account.models import Account

def register(request):
    if request.method == POST:
        # Wypada w tym miejscu dodac walidacje danych
        new_user = Account()
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.email = request.POST['email']
        new_user.password_hash = str(hashlib.sha512(request.POST['password']))
        new_user.active = False
        new_user.activation_code
    else:
        # Tutaj powinnismy wygenerowac formularz, np. korzystajac z szablonow Django
        return HttpResponse('Not implemented')

def login(request):
    return HttpResponse('Not implemented')
