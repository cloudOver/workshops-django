from django.conf.urls import url
from django.contrib import admin

import account.views

urlpatterns = [
    url(r'register/$', account.views.register, name='account_register'),
    url(r'login/$', account.views.login, name='account_login'),
]
