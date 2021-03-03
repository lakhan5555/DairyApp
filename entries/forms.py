from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'textarea', 
        'placeholder': 'What/s on your mind?'})
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username','email','password1','password2']
        