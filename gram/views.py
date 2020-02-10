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


@login_required(login_url='/accounts/login')
def delete_post(request, image_id):
    '''
    View function to delete an image post
    '''
    remove = Image.objects.get(id=image_id)
    remove.delete()
    return redirect(index)


@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user  # get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user)

        pics = Image.objects.filter(user=request.user.id).all()

    except:

        title = f'{current_user.username}'

        pics = Image.objects.filter(user=request.user.id).all()

        info = Profile.objects.filter(user=7)

    return render(request, 'my-profile.html', {"title": title, "current_user": current_user, "info": info, "pics": pics})


@login_required(login_url='/accounts/login')
def other_profile(request, prof_id):
    '''
    View function to display a profile information of other users
    '''
    current_user = request.user

    try:

        info = Profile.objects.filter(id=prof_id)

        follow_profile = Profile.objects.get(id=prof_id)

        check_if_following = Follow.objects.filter(
            user=current_user, profile=follow_profile).count()

        pics = Image.objects.all().filter(user_id=prof_id)
        nbr = pics.count()

        title = f'{request.user.username}\'s'

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'other-profile.html', {"title": title, "nbr": nbr, "current_user": current_user, "info": info, "pics": pics, "check_if_following": check_if_following})
