from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    body = models.TextField()
    tag = models.ManyToManyField('Tag')
    cretaed = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True,editable=False)


    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering =['-cretaed']





class Tag(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='icons/',null=True,blank=True)
    slug = models.SlugField(max_length=200,unique=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering =['order']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, max_length=300)
    phone = models.CharField(max_length=13)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    brith_date = models.DateField(null=True, blank=True)
    varified_email = models.BooleanField(default=False)


    def __str__(self):
        return f"Profile of {self.user.username}"
    