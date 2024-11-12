from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from BlogApp.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from .models import BlogPost
from .forms import BlogPostForm



# Create your views here.


def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Get all posts, newest first
    return render(request, 'BlogApp/post_list.html', {'posts': posts})  # Pass posts to the template

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)  # Get the post by primary key or return 404
    return render(request, 'BlogApp/post_detail.html', {'post': post})



@login_required
def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'BlogApp/post_form.html', {'form': form})



@login_required
def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'BlogApp/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()  # Delete the post
        return redirect('home')  # Redirect to the homepage after deletion
    return render(request, 'BlogApp/post_confirm_delete.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'BlogApp/register.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home or another page after signup
    else:
        form = UserCreationForm()
    return render(request, 'templates/registration/signup.html', {'form': form})
