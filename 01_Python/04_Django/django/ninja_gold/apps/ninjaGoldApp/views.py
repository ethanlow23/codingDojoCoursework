# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from time import strftime, gmtime

# Create your views here.
def index(request):
    return render(request, 'ninjaGoldApp/ninja_gold.html')

def process(request):
    if request.method == 'POST':
        if 'gold' not in request.session:
            request.session['gold'] = 0
        if 'activities' not in request.session:
            request.session['activities'] = []

        if request.POST['get_gold'] == 'farm':
            randNum = random.randint(10,21)
            request.session['gold'] += randNum
            request.session['activities'].insert(0, 'Entered farm and earned ' + str(randNum) + ' gold. ' + strftime('%Y/%m/%d %I:%M %p', gmtime()))
        if request.POST['get_gold'] == 'cave':
            randNum = random.randint(5, 11)
            request.session['gold'] += randNum
            request.session['activities'].insert(0, 'Entered cave and earned ' + str(randNum) + ' gold. ' + strftime('%Y/%m/%d %I:%M %p', gmtime()))
        if request.POST['get_gold'] == 'house':
            randNum = random.randint(2, 6)
            request.session['gold'] += randNum
            request.session['activities'].insert(0, 'Entered house and earned ' + str(randNum) + ' gold. ' + strftime('%Y/%m/%d %I:%M %p', gmtime()))
        if request.POST['get_gold'] == 'casino':
            randNum = random.randint(-50, 51)
            request.session['gold'] += randNum
            request.session['activities'].insert(0, 'Entered casino and it was too much to code out')

    return redirect('/')