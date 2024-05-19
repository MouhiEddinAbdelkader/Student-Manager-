from django import forms

from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    nom = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    prenom = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    email = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    telephone = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['nom','prenom', 'email', 'telephone' ,'avatar', 'bio']