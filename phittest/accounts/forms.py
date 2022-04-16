from django import forms

class LoginForm(forms.Form):
    """Contains definition for the Login form.

    Args:
        Form (Class): Form class
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
