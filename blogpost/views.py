# -*-coding:utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from models import Blogpost

# Create your views here.
def index(request):
    context= {'posts': Blogpost.objects.all()[:5]}
    return render(request, 'index.html', context)

def view_post(request, slug):
    context= {'post': get_object_or_404(Blogpost, slug=slug)}
    return render(request, 'blogpost_details.html', context)