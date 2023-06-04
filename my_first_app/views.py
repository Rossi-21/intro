from django.shortcuts import render, HttpResponse, redirect
from django.core.serializers import serialize
from django.http import JsonResponse
import requests
from . import models


def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("Hello Blog!")

def new (request):
    return HttpResponse("Form to create a new blog")

def create (request):
    return redirect("/")

def show (request, id):
    return HttpResponse("placeholder to display blog number: {number}")

def edit (request, id):
    return HttpResponse("placeholder to edit blog {number}")

def destroy (request, id):
    return redirect("/")

def json (request):
    obj = models.objects.first()
    data = serialize("json", [obj], fields=('title', 'content'))
    return HttpResponse(data, content_type="application/json")

