# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1 or not postData['first_name'].isalpha():
            errors['first_name'] = 'Enter a name'
        if len(postData['last_name']) < 1 or not postData['last_name'].isalpha():
            errors['last_name'] = 'Enter your last name'
        if not EMAIL_REGEX.match(postData['email']) or len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = 'Enter a valid email'
        if len(postData['password']) < 8:
            errors['password'] = 'password must be at least 8 characters'
        if not postData['password'] == postData['confirm_pw']:
            errors['confirm_pw'] = 'passwords do not match'
        return errors

    def login_validator(self, postData):
        login_errors = {}
        hash1 = bcrypt.hashpw(postData['pw_login'].encode(), bcrypt.gensalt())
        if len(User.objects.filter(email=postData['email_login'])) == 0 or not bcrypt.checkpw(postData['pw_login'].encode(), hash1.encode()):
            login_errors['login'] = 'Incorrect email or password. Try again'
        return login_errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.IntegerField()
    user = models.ManyToManyField(User, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name='reviews')
    book = models.ForeignKey(Book, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)