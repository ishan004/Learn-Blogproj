from blog.forms import commentform
from .forms import commentform
from .models import Post, comment
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(req):
    posts = Post.objects.all()
    
    context  = {
        'posts' : posts
    } 

    return render(req, 'index.html', context = context)


def post_detail(req, post_slug):
    post = Post.objects.get(slug=post_slug)

    

    if req.method == 'POST':
        comment_form = commentform(data=req.POST)
        if comment_form.is_valid():
          
            comment_new = comment_form.save(commit=False)
            comment_new.post = post 
            comment_new.save()   

    else:
        comment_form = commentform()

    context = {
        'post' : post,
        'comment_form' : comment_form
    }
    return render(req, 'detail.html', context = context)
