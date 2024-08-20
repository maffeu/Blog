from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from users.models import UserProfile


@login_required(login_url='login')
def post_list(request):
    postList = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
           user = request.user
           print(user.username)
           user_profile = UserProfile.objects.get(user=user)

           post = form.save(commit=False)
           post.user = user_profile
           post.save()

           return redirect('postList')
        
    context = {'posts':postList, 'form':form }
    return render(request, 'posts/post_list.html',context)

def post_details(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'posts/details.html', {'post':post})

def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    if post:
        post.delete()
        return redirect('postList')
    else:
        return HttpResponse('Post not found')
    
def updatePost(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('postList')
    context = {'update_form':form} 
    return render(request, 'posts/update.html', context)   


