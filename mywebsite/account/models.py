from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    active = models.BooleanField(default=False, help_text='Is account activated through email')
    activacion_code = models.CharField(max_length=60, default='', blank=True, null=True, help_text='Code used to activate account with email')
    
    password_hash = models.CharField(max_length=60, help_text='sha512 of password + salt')
    
