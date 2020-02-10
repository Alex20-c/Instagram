from django.shortcuts import render, redirect
from django.http  import HttpResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Image, Comment, Like, Follow
from .forms import ImagePostForm, CommentForm, ProfileForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.

def base(request):
    return render(request, 'base.html')


def explore(request):
    '''
    Views the initial profile
    '''
    images = Image.objects.all()
    return render(request, 'explore.html', {"images":images})


@login_required(login_url='/accounts/login')
def timeline(request):
    '''
    returns timeline html
    '''
    return render(request, 'timeline.html')


@login_required(login_url='/accounts/login')
def index(request):
    # images = Image.get_images()
    current_user = request.user

    title = 'One piece'

    # user_info = Profile.objects.get(user=current_user.id)

    grammers = Profile.get_profiles

    following = Follow.get_following(current_user.id)

    images = []
    for followed in following:
        # get profile id for each and use it to find user id
        profiles = Profile.objects.filter(id=followed.profile.id)
        for profile in profiles:
            post = Image.objects.filter(user=profile.user)

            for image in post:
                images.append(image)

    return render(request, 'index.html', {"images": images, "title": title, "following": following, "user": current_user, "grammers": grammers})

@login_required(login_url='/accounts/login')
def single_image(request, photo_id):
    '''
    View funtion to display a particular image with its details
    '''
    image = Image.objects.get(id=photo_id)
    # fetch the profile of the user who posted
    user_info = Profile.objects.get(user=image.user.id)
    comments = Comment.objects.filter(post=image.id)
    validate_vote = Like.objects.filter(
        user=request.user, post=photo_id).count()
    upvotes = Like.get_post_likes(image.id)
    likes = len(upvotes)
    return render(request, 'single-image.html', {'image': image, "user_info": user_info, "comments": comments, "likes": likes, "validate_vote": validate_vote})


@login_required(login_url='/accounts/login')
def manage_image(request, photo_id):
    '''
    View funtion to display a particular image with its details
    '''
    image = Image.objects.get(id=photo_id)
    user_info = Profile.objects.get(user=image.user.id)
    comments = Comment.objects.filter(post=image.id)
    validate_vote = Like.objects.filter(user=request.user, post=photo_id).count()
    upvotes = Like.get_post_likes(image.id)
    likes = len(upvotes)
    return render(request, 'manage-image.html', {'image': image, "user_info": user_info, "comments": comments, "likes": likes, "validate_vote": validate_vote})
