# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
# /users
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'restUsersApp/restful_users.html', context)
# /users/new
def new(request):
    return render(request, 'restUsersApp/users_add.html')
# /users/<id>/edit
def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'restUsersApp/users_edit.html', context)
# /users/<id>
def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'restUsersApp/users_show.html', context)
# /users/create
def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/users/new')
        else:
            new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            id = new_user.id
            return redirect('/users/' + str(id))
# /users/<id>/destroy
def destroy(request, id):
    x = User.objects.get(id=id)
    x.delete()
    return redirect('/users')
# /users/<id>/update
def update(request, id):
    if request.method == 'POST':
        edit = User.objects.get(id=id)
        edit.first_name = request.POST['first_name']
        edit.last_name = request.POST['last_name']
        edit.email = request.POST['email']
        edit.save()
    return redirect('/users/' + str(id))