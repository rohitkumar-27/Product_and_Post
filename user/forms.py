from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Post


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]




class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']