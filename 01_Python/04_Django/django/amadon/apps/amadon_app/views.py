# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'amadon_app/amadon.html')

def buy(request):
    if request.method == 'POST':
        if 'total' not in request.session:
            request.session['total'] = 0
        if 'count' not in request.session:
            request.session['count'] = 0
        if 'price' not in request.session:
            request.session['price'] = 0
        
        if request.POST['product'] == 'shirt':
            request.session['total'] += 19.99 * int(request.POST['quantity'])
            request.session['price'] = 19.99 * int(request.POST['quantity'])
        elif request.POST['product'] == 'sweater':
            request.session['total'] += 29.99 * int(request.POST['quantity'])
            request.session['price'] = 29.99 * int(request.POST['quantity'])
        elif request.POST['product'] == 'cup':
            request.session['total'] += 4.99 * int(request.POST['quantity'])
            request.session['price'] = 4.99 * int(request.POST['quantity'])
        else: #request.POST['product'] == 'book':
            request.session['total'] += 49.99 * int(request.POST['quantity'])
            request.session['price'] = 49.99 * int(request.POST['quantity'])
        
        request.session['count'] += int(request.POST['quantity'])
    return redirect('/result')

def result(request):
    return render(request, 'amadon_app/result.html')