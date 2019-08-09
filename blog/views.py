from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "author": "Dan",
        'title': "Test",
        "content": "Hello World!",
        'date_posted': "Today"
    },
    {
        "author": "Jane",
        'title': "Test2",
        "content": "Hello Moscow!",
        'date_posted': "Yesterday"
    },
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})