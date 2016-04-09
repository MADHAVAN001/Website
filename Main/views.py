from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template import Context
from django.core.urlresolvers import reverse_lazy

def homepage(request):
    return render(request, 'homepage.html')

def google(request):
    return render(request, 'google064842d463096bf5.html')

def explorations(request):
    return render(request, 'explorations.html')

def entrepreneurship(request):
    return render(request, 'entrepreneurship.html')