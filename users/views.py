from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'users/user-profile.html', {'profile': profile})

@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    posts = profile.post_set.all()
    context = {'profile': profile, 'posts': posts}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def edit_account(request):
    profile= request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile-form.html', context)


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'username or pasword incorrect')

    return render(request, 'users/login-register.html')

def logout_user(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('profiles')

def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('edit-account')
        else:
            messages.success(request, 'An error occured during signup')

    context ={'page': page, 'form': form}
    return render(request, 'users/login-register.html', context)
