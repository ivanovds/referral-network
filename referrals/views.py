from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Referral


@login_required()
def referral_view(request):

    context = {}
    return render(request, "referrals.html", context)

