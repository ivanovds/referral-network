from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .forms import ProfileForm, UserRegisterForm, LoginForm
from .models import Profile, ProfileImage
from referrals.models import Referral


def register_view(request):
    if request.method == 'POST':
        sign_up_form = UserRegisterForm(request.POST or None)
        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
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
        if Profile.objects.filter(ref_code=ref_code).exists():
            request.session['ref_code'] = ref_code

    context = {
        'sign_up_form': sign_up_form,
    }
    return render(request, 'register.html', context)


def login_view(request):
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
                    return redirect('/')
                else:
                    messages.error(request, "No referrer with this referral code.")
        else:
            messages.error(request, "Email or password is invalid.")
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


@login_required()
def profile_list(request):
    queryset_list = Profile.objects.filter(~Q(user=request.user))

    paginator = Paginator(queryset_list, 25)  # Show 25 profiles per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, "profile_list.html", context)


@login_required()
def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    images = ProfileImage.objects.filter(profile=profile)[::-1]
    context = {
        "profile": profile,
        'images': images,
    }
    return render(request, "profile_detail.html", context)


@login_required()
def my_profile(request):
    profile = get_object_or_404(Profile, id=request.user.id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            images = request.FILES.getlist('image')
            if images:
                profile.avatar = images[-1]
                profile.save(update_fields=["avatar"])

                for img in images:
                    profile_img = ProfileImage(image=img, profile=profile)
                    profile_img.save()

            form.save()
            messages.success(request, "Successfully Updated.")
            return redirect('/')
        else:
            messages.error(request, "Profile was not updated.")
            return redirect('/')

    images = ProfileImage.objects.filter(profile=profile)[::-1][1:]

    context = {
        'form': form,
        'images': images,
        'profile': profile,
    }

    return render(request, "my_profile.html", context)
