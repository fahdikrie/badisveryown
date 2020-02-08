from django import forms
from . import models


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='name',widget=forms.TextInput(
        attrs={
            'class' : 'form-control form-control',
            'placeholder' : 'name...',
            'style' : 'width: 50vw;'
        }, 
    ))

    email = forms.CharField(label='email',widget=forms.TextInput(
        attrs={
            'class' : 'form-control form-control',
            'placeholder' : 'email...',
            'style' : 'width: 50vw;'
        }, 
    ))

    body = forms.CharField(label='tell me something good!',widget=forms.Textarea(
        attrs={
            'class' : 'form-control form-control',
            'placeholder' : 'write your comment here...',
            'style' : 'height: 10vh; overflow: auto!important; width: 50vw;',
        }, 
    ))

    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'body')