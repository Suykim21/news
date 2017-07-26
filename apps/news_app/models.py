# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
  def sub(self, data):
    errors = []

    if len(data['name']) < 2:
      errors.append('Name must be at least two characters long')
    if not data['name'].isalpha():
      errors.append('Name can only be letters')

    if not EMAIL_REGEX.match(data['email']):
      errors.append('Please enter valid email address')

    try:
      User.objects.get(email=data['email'])
      errors.append('Email is already subscribed, please input another email')
    except:
      pass

    if len(errors) == 0:
      new_subscriber = User.objects.create(name=data['name'], email=data['email'])

      return {
        'new': new_subscriber,
        'error_list': None
      }
    else:
      return {
        'new': None,
        'error_list': errors
      }

class User(models.Model):
  name = models.CharField(max_length=40)
  email = models.EmailField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
