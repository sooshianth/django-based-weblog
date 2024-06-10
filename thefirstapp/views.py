from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm

def index(request):
    return HttpResponse('<h1> this is my index page</h1>')

def home(request):
    return HttpResponse('<h2>This page has been written by <a href="https://t.me/itstyrmo"> Tyrmo</a></h2>')

def post_page(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_page/post_page.html', context=context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comment}
    return render(request, 'post_page/post_detail.html', context=context)

def post_addition(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'post_page/post_addition.html', {'form': form})