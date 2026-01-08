from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from.forms import *
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
# Create your views here.

def home_view(request):

    posts = Post.objects.all()
    return render(request, 'a_posts/home.html',{'posts':posts})


def post_create_view(request):

    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

             # concent the to we Webcrawler
            website = requests.get(form.data['url']) # concent the to we Webcrawler
            sourccode= BeautifulSoup(website.text, 'html.parser') 

            # select the element that we want to add to post
            find_image = sourccode.select('meta[content^="https://live.staticflickr.com/"]')
            image= find_image[0] ['content']
            post.image = image

            find_title = sourccode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title

            find_artist = sourccode.select('a.owner-name')
            artist = find_artist[0].text.strip() # we use the text for conveting list 1st element into the text and strip for removing the white text
            post.artist=artist[0].strip()
            form.save()
            return redirect('home')
    return render(request,'a_posts/post_create.html',{'form':form})

def post_delet(request,pk):
    post = get_object_or_404(Post, id=pk)
    if request.method== 'POST':
        post.delete()
        messages.success(request,'Post Deleted')
        return redirect('home')


    return render(request, 'a_posts/post_delet.html',{'post':post})

def edit_post_view(request,pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditFrom(instance=post)

    if request.method == 'POST':
        form=PostEditFrom(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'sucessfull edit')
            return redirect('home')
    context={

        'post': post,
        'form': form
    }
    return render(request,'a_posts/edit_post.html',context)    

def post_page_view(request,pk):
    post = get_object_or_404(Post, id=pk)
    return render(request,'a_posts/post_page.html',{'post':post})


