from django.forms import ModelForm,forms
from django import forms
from.models import *


class PostCreateForm(ModelForm):
    class Meta():
        model = Post
        fields = ['url','body','tag']
        labels ={
            'body' : 'Caption',
            'tag' :'Category'
        }   

        widgets = {

            'body' : forms.Textarea(attrs={'rows':3,'placeholder':'write a caption......','class':'font1 text-4xl'}),
            'tag':forms.CheckboxSelectMultiple({
            'class': 'modern-checkbox'
        }),
        }

class PostEditFrom(ModelForm):
    class Meta():
        model = Post
        fields = ['body','tag']
        labels ={
            'body' : 'Caption',
            'tag':'Category'
        }

        widgets = {

            'body' : forms.Textarea(attrs={'rows':3,'placeholder':'write a caption......','class':'font1 text-4xl'}),
             'tag':forms.CheckboxSelectMultiple(),
        }

class CustamSignupForm(forms.Form):
    phone = forms.CharField(max_length=13, required=True, label='Phone Number')
   
   
    def signup(self, request, user):
        porfile = UserProfile(user=user)
        porfile.phone = self.cleaned_data.get('phone','')
        porfile.save()