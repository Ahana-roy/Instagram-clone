from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db import transaction
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login


from post.models import Post, Follow, Stream
from django.contrib.auth.models import User
from authy.models import Profile
from .forms import EditProfileForm, UserRegisterForm
from django.urls import resolve
from comment.models import Comment



# creating view for new or existing user profile and to check wheather follow status is true or not

def UserProfile(request, username):
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    posts = Post.objects.filter(user=user)

    
    if url_name == 'profile':
        posts = Post.objects.filter(user=user)
    else:
        posts = profile.favourite.all()
    
        

    # Profile Stats
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()
   
    
    
    # checking if user follows another user or not
     
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    status = list(Follow.objects.values('status').filter(following=user, follower=request.user))
    print(status)
    global status_val
    for i in status:
        for status, items in i.items():
            status_val = items

    print(status_val)
    # pagination
    # paginator = Paginator(posts, 8)
    # page_number = request.GET.get('page')
    # posts_paginator = paginator.get_page(page_number)

    
    context = {
        'posts': posts,
        'profile':profile,
        'posts_count':posts_count,
        'following_count':following_count,
        'followers_count':followers_count,
       # 'posts_paginator':posts_paginator,
        'follow_status':follow_status,
        'status_val' : status_val
    }
    return render(request, 'profile.html', context)



# editing profile for existing user

def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method == "POST":
        
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
       
        if form.is_valid():
            
            profile.image = form.cleaned_data.get('image')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            form.save()
            
            return redirect('profile', profile.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'form':form,
    }
    return render(request, 'editprofile.html', context)



# views for follow 

def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)

    print(following,option)
    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following, user=request.user).all().delete()
        else:
            posts = Post.objects.all().filter(user=following)[:25]
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=request.user, date=post.posted, following=following)
                    stream.save()
        return HttpResponseRedirect(reverse('profile', args=[username]))

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile', args=[username]))


    
# views for new user registration
    
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, 'Hurray your account is created!!')

            
            # Automatically Log In The User

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            
            login(request, new_user)
           
            return redirect('index')
            


    elif request.user.is_authenticated:
        return redirect('index')
    
    else:
        form = UserRegisterForm()


    context = {
        'form': form,
    }
    return render(request, 'sign-up.html', context)