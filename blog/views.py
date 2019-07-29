from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
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


class PostCreateView(LoginRequiredMixin, CreateView): #Order matters 
    model = Post 
    fields = ['title', 'content']

    # hur dur polymorpishm hurr
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs CreateView's version of from_valid


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

        

def about(request):
    return render(request, 'blog/about.html',)




