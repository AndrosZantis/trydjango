# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#make html work
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#a place to handle various web pages
#you can have as many views as you want
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "about.html", {})
