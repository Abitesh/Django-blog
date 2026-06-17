from django.shortcuts import render
from django.http import HttpResponse
from .models import post


#A list of dictinoary each associated with information of a post
posts = [
    {
        'author':'Abi',
        'title':'Learning Django',
        'content':'In th e part3 video template learning',
        'Date_posted':'12-07-2026'
    },
    {
        'author':'Abi',
        'title':'Learning Django',
        'content':'In th e part3 video template learning',
        'Date_posted':'12-07-2026'
    },
    {
        'author':'Tesh',
        'title':'Learning Django',
        'content':'In th e part2 video routes learning',
        'Date_posted':'12-07-2026'
    }
]

def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})