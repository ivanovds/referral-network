"""Referrals Models

A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""

from django.db import models
from django.contrib.auth.models import User


class Referral(models.Model):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrers')
    referral = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')

    class Meta:
        unique_together = (('referrer', 'referral'),)
