from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post,Blood,Organs



def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def blood(request):
    context={
        'posts':Blood.objects.all()
    }
    return render(request,'blog/bloodpost.html',context)

def organs(request):
    context={
        'posts':Organs.objects.all()
    }
    return render(request,'blog/organspost.html',context)
class PostListView(ListView):
    model=Post
    template_name='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'  #A way to refer to the object
    ordering=['-date_posted']
    paginate_by=5

class BloodPostListView(ListView):
    model=Blood
    template_name='blog/bloodpost.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'  #A way to refer to the object
    ordering=['-date_posted']
    paginate_by=5


class OrgansPostListView(ListView):
    model=Organs
    template_name='blog/Organspost.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'  #A way to refer to the object
    ordering=['-date_posted']
    paginate_by=5
    
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html' 
    context_object_name = 'posts'  
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class BloodUserPostListView(ListView):
    model=Blood
    template_name='blog/blood_user_post.html' 
    context_object_name = 'posts'  
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class OrgansUserPostListView(ListView):
    model=Organs
    template_name='blog/organ_user_post.html' 
    context_object_name = 'posts'  
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
class PostDetailView(DetailView):
    model=Post
    
class BloodPostDetailView(DetailView):
    model=Blood
    
class OrgansPostDetailView(generic.DetailView):
    model=Organs


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class BloodPostCreateView(LoginRequiredMixin,CreateView):
    model=Blood
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class OrgansPostCreateView(LoginRequiredMixin,CreateView):
    model=Organs
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class BloodPostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Blood
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class OrgansPostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Organs
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class BloodPostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Blood
    success_url='/'
    
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class OrgansPostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Organs
    success_url='/'
    
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
def contact(request):
    return render(request,'blog/contact.html',{'title':'Contact'})