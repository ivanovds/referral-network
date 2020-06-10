from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ProfileForm
from .models import Profile, ProfileImage


@login_required()
def profile_list(request):
    """List of all existing profiles except the profile of current user."""
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
    """View with all detail profile information.

    Returns 404 error if profile does not exist.
    Displays profile images in order from last to first added.
    """
    profile = get_object_or_404(Profile, id=profile_id)
    images = ProfileImage.objects.select_related('profile').filter(profile=profile)[::-1][1:]  # [1:] - exclude avatar
    context = {
        "profile": profile,
        'images': images,
    }
    return render(request, "profile_detail.html", context)


@login_required()
def my_profile(request):
    """View with current user profile.

    Allowed methods: GET, POST.
    GET: displays avatar, all previous avatars, profile information, form to update profile.
    POST: saves only updated fields. Allows to add multiple photos, saves the last one as an avatar to
    Profile model`s field "avatar". Saves all added photos to ProfileImage model.
    """
    profile = get_object_or_404(Profile, id=request.user.profile.id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            images = request.FILES.getlist('image')
            if images:
                profile.avatar = images[-1]
                profile.save(update_fields=["avatar"])

                for img in images:
                    ProfileImage.objects.create(image=img, profile=profile)

            form.save()
            messages.success(request, "Successfully Updated.")
            return redirect('/')
        else:
            messages.error(request, "Profile was not updated.")
            return redirect('/')

    images = profile.profile_images.all()[::-1][1:]  # [1:] - exclude avatar

    context = {
        'form': form,
        'images': images,
        'profile': profile,
    }

    return render(request, "my_profile.html", context)
