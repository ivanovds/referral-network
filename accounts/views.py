from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .forms import UserRegisterForm, LoginForm
from referrals.models import Referral
from profiles.models import Profile


def register_view(request):
    """Register view for creating new user.

    Requires unique email.
    Password should satisfy standard Django password validators.
    Transforms entered email to username (username - first part of email up to "@").

    GET: Writes ref_code into request.session if there is a "?ref=<ref_code>" in the URl.
    POST: If there is a ref_code in request.session and it is valid, saves a Referral object.
    """
    if request.method == 'POST':
        sign_up_form = UserRegisterForm(request.POST or None)
        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, "User with this email already exists.")
            else:
                password = sign_up_form.cleaned_data.get('password1')
                username = (email.lower()).split("@")[0]
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()

                ref_code = request.session.get('ref_code')
                if ref_code:
                    try:
                        referrer = Profile.objects.get(ref_code=ref_code)
                    except ObjectDoesNotExist:
                        messages.info(request, "No referrer with this referral code.")
                    else:
                        Referral.objects.create(
                            referrer=referrer.user,
                            referral=user,
                        )

                login(request, user)
                return redirect('/')

    else:
        sign_up_form = UserRegisterForm()
        ref_code = request.GET.get('ref', '')
        if ref_code:
            if Profile.objects.filter(ref_code=ref_code).exists():
                request.session['ref_code'] = ref_code
            else:
                messages.info(request, "No referrer with this referral link!")

    context = {
        'sign_up_form': sign_up_form,
    }
    return render(request, 'register.html', context)


def login_view(request):
    """User authentication.

    Requires email and password to be entered,
    but uses username and password for authentication.
    """
    if request.method == 'POST':
        log_in_form = LoginForm(request.POST or None)
        if log_in_form.is_valid():
            email = log_in_form.cleaned_data.get('email')
            try:
                username = User.objects.get(email=email.lower()).username
            except ObjectDoesNotExist:
                messages.error(request, "No user with this email.")
            else:
                password = log_in_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect(request.GET.get('next', 'home'))
                else:
                    messages.error(request, "Password is invalid.")
    else:
        log_in_form = LoginForm()

    context = {
        'log_in_form': log_in_form,
    }

    return render(request, 'login.html', context)


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')

