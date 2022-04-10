from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User

=======
>>>>>>> be8bda85bcc865affa2b67d8e65a6c9ffd05e4d7
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

<<<<<<< HEAD

class SearchForm(forms.Form):
    query = forms.CharField()


class UserRegistrationForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
=======
>>>>>>> be8bda85bcc865affa2b67d8e65a6c9ffd05e4d7
