from django.shortcuts import render

from accounts.forms import LoginForm


def login_view(request):
    """Shows Login page, and should be available to all users."""
    form = LoginForm(request.POST or None)
    return render(request, 'login.html', {'form': form})