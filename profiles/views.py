from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ProfileForm
from .models import Profile, ProfileImage


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
    images = ProfileImage.objects.filter(profile=profile)[::-1][1:]
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
