from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "posts/home.html", context)

@login_required(login_url='login')
def create_post(request):
    profile = request.user.profile
    form = PostForm()

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = profile
            post.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'posts/post-form.html', context)

def detail_post(request, pk):
    post =Post.objects.get(id=pk)
    return render(request, 'posts/post-detail.html', {'post': post})

@login_required(login_url='login')
def update_post(request, pk):
    profile = request.user.profile
    try:
        post = profile.post_set.get(id=pk)
        form = PostForm(instance=post)
    

        if request.method =='POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
    
        context = {'form': form}
        return render(request, 'posts/post-form.html', context)
    except:
        return redirect('home')
   

@login_required(login_url='login')
def delete_post(request, pk):
    profile = request.user.profile
    post = profile.post_set.get(id=pk)
    if request.method =='POST':
        post.delete()
        return redirect('home')
        
    context = {'post': post}
    return render(request, 'posts/delete-post.html', context)