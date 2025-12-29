from django.shortcuts import render,redirect
from.models import Post
from django.forms import ModelForm
from django import forms
from bs4 import BeautifulSoup
import requests
# Create your views here.

def home_view(request):

    posts = Post.objects.all()
    return render(request, 'a_posts/home.html',{'posts':posts})


class PostCreateForm(ModelForm):
    class Meta():
        model = Post
        fields = ['url','body']
        labels ={
            'body' : 'Caption'
        }

        widgets = {

            'body' : forms.Textarea(attrs={'rows':3,'placeholder':'write a caption......','class':'font1 text-4xl'}),
        }


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