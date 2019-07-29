from django.shortcuts import render
from blog.models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView 
)  #Anlagous to Index, Show, and Create on rails


# Create your views here.
def home(request):
    context = {
        "posts": Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering=['-date_updated']


class PostDetailView(DetailView):
    model = Post 

class PostCreateView(CreateView):
    model = Post 
    fields = ['title', 'content']


def about(request):
    return render(request, 'blog/about.html',)




