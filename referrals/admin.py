"""Admin interface

The Django admin application can use your models to automatically build a site area
that you can use to create, view, update, and delete records. This can save you
a lot of time during development, making it very easy to test your models
and get a feel for whether you have the right data.
"""


from django.contrib import admin
from .models import Referral


class ReferralModelAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "referral", "referrer"]
    list_filter = ["timestamp"]

    class Meta:
        model = Referral


admin.site.register(Referral, ReferralModelAdmin)

