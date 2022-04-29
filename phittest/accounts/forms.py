from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Contains definition for the Login form.

    Args:
        Form (Class): Form class
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'username', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'password', 'placeholder':'Password'}))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user