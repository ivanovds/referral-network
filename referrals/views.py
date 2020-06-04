from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Referral


@login_required()
def referral_view(request):
    ref_list = Referral.objects.filter(referrer=request.user)
    ref_count = ref_list.count()
    context = {
        'ref_count': ref_count,
        'ref_list': ref_list,
    }
    return render(request, "referrals.html", context)

