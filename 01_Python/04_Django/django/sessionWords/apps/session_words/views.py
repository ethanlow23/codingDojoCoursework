# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'session_words/session_words.html')

def modify(request):
    if request.method == 'POST':
        if 'word' not in request.session:
            request.session['word'] = [request.POST['word']]
        else:
            request.session['word'].insert(0, request.POST['word'])
        
        request.session['color'] = ''
        if request.POST['color'] == 'red':
            request.session['color'] = 'red'
        elif request.POST['color'] == 'green':
            request.session['color'] = 'green'
        else:
            request.session['color'] = 'blue'
        
        if 'font' not in request.POST:
            request.session['bold'] = 'normal'
        else:
            request.session['bold'] = 'bold'
        return redirect('/')