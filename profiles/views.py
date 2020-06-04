from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm


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
    instance = get_object_or_404(Profile, id=profile_id)
    # if instance.publish > timezone.now().date():
    #     if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    context = {
        "instance": instance,
    }
    return render(request, "profile_detail.html", context)


@login_required()
def home_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = ProfileForm()

    context = {
        "form": form,
    }
    return render(request, "home_view.html", context)


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
            login(request, user)
            return redirect('/')

    else:
        sign_up_form = UserRegisterForm()
        ref_code = request.GET.get('ref', 'no code')
        if Profile.objects.filter(ref_code=ref_code).exists():
            request.session['ref_code'] = ref_code

        print(request.session['ref_code'])

    context = {
        'sign_up_form': sign_up_form,
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        log_in_form = LoginForm(request.POST or None)
        if log_in_form.is_valid():
            email = log_in_form.cleaned_data.get('email')
            username = User.objects.get(email=email.lower()).username
            password = log_in_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                #  TODO: invalid login or password message
                pass
    else:
        log_in_form = LoginForm()

        print(request.session['ref_code'])

    context = {
        'log_in_form': log_in_form,
    }

    return render(request, 'login.html', context)


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')
