# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt

# Create your views here.
def index(request): # /
    request.session.clear()
    return render(request, 'beltReviewerApp/index.html')

def register(request): # /process
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hash1)
            user = User.objects.get(email=request.POST['email'])
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
        return redirect('/books')

def login(request): # /process_login
    if request.method == 'POST':
        login_errors = User.objects.login_validator(request.POST)
        if len(login_errors):
            for tag, error in login_errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email_login'])
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('/books')

def result(request): # /result
    if 'first_name' not in request.session:
        return redirect('/')
    else:
        return render(request, 'beltReviewerApp/books.html')

def books(request): # /books
    if 'first_name' not in request.session:
        return redirect('/')
    context = {
        'books': Book.objects.order_by('created_at')
    }
    return render(request, 'beltReviewerApp/books.html', context)

def add(request): # /add
    if 'first_name' not in request.session:
        return redirect('/')
    return render(request, 'beltReviewerApp/add.html')

def reviews(request, id): # /books/<id>
    if 'first_name' not in request.session:
        return redirect('/')
    context = {
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(book=id)
    }
    return render(request, 'beltReviewerApp/reviews.html', context)

def users(request, id): # /users/<id>
    if 'first_name' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'beltReviewerApp/users.html', context)

def book_review(request): # /book_review
    if 'first_name' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        new_book = Book.objects.create(title=request.POST['title'], author=request.POST['author'], rating=(request.POST['rating']))
        id = new_book.id
        Review.objects.create(content=request.POST['review'], user=User.objects.get(id=request.session['id']), book=Book.objects.get(id=id))
    return redirect('/books/' + str(id))

def new_review(request, id): # /new_review/<id>
    if 'first_name' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        Review.objects.create(content=request.POST['add_review'], user=User.objects.get(id=request.session['id']), book=Book.objects.get(id=id))
        return redirect('/books/' + str(id))

def delete(request, id): # /delete/<id>
    if 'first_name' not in request.session:
        return redirect('/')
    book_id = Review.objects.get(id=id).book.id
    Review.objects.get(id=id).delete()
    return redirect('/books/' + str(book_id))