from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def all_members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
