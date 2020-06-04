"""Referral URL Configuration"""


from django.urls import path
from referrals.views import referral_view


urlpatterns = [
    path('', referral_view, name='referrals'),
]
