# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses_app/courses.html', context)

def add(request):
    if request.method == 'POST':
        errors = Course.objects.course_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            Course.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('/')

def delete(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses_app/delete_course.html', context)

def confirm_delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')