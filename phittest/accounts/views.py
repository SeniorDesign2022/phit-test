from asyncio.log import logger
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages



from accounts.forms import LoginForm, RegisterForm


def login_view(request):
    """Shows Login page, and should be available to all users."""
    form = LoginForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='doctor'):
                    return redirect(reverse('pages:patients'))
                return redirect(reverse('pages:dashboard'))
            else:
                # This code can be used in order to determine
                # if a user has tried logging in more than once
                # attempt = request.session.get('attempt') or 0
                # request.session['attempt'] = attempt + 1
                logger.warning(f'Failed to login user {username}')
                # request.session['invalid user'] = 1
                # form.add_error('password', ValidationError(
                #     validationErrors.WRONG_PASS.label,
                #     code=validationErrors.WRONG_PASS
                # ))
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """Handles logging out the user and re-routes to login page."""
    logout(request)
    return redirect(reverse('login'))


def register_view(request):
    request.session['account_created'] = None

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['account_created'] = user.username
            messages.success(request, "Registration successful.")
            return redirect(reverse("register_success"))
        messages.error(request, "Unsuccessful registration. Invalid information.")
        
    form = RegisterForm()
    return render (request, "accounts/register.html", {"form":form})


def register_success_view(request):
    return render(request, 'accounts/register_success.html')