from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.text import slugify

blog_posts = { 
    "Introduction": "Welcome to my blog! This is the first post.",
    "Blog Purpose": "This blog will serve as a platform to share my thoughts and experiences.",
    "App": "Did you know that Django is a powerful web framework for building web applications? The App itself might refer to whole app,  but actually it might refers to module",
}

def home(request):
    return render(request, 'home.html')

def all_blogs(request):
    posts = [(slugify(title),title) for title in blog_posts.keys()]
    return render(request, 'blog/all_blogs.html', {'posts': posts})

def blog_detail(request, slug):
    for title, content in blog_posts.items():
        if slugify(title) ==  slug:
            return render(request, 'blog/blog_detail.html', {'title': title, 'content': content,})
    raise Http404("Blog post not found")


