from asyncio.log import logger
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse


from accounts.forms import LoginForm


def login_view(request):
    """Shows Login page, and should be available to all users."""
    form = LoginForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(
                    f'Successful login by user {username} who belongs to groups '
                    f'{",".join(str(group) for group in user.groups.all())}')
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