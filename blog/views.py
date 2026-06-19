from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


#A list of dictinoary each associated with information of a post
Posts = [
    {
        'author':'Abi',
        'title':'Learning Django',
        'content':'In th e part3 video template learning',
        'Date_posted':'12-07-2026'
    },
    {
        'author':'akilesh',
        'title':'Learning 2nd post',
        'content':'In th e part 4  video template learning',
        'Date_posted':'12-07-2029'
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
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})