"""Admin interface

The Django admin application can use your models to automatically build a site area
that you can use to create, view, update, and delete records. This can save you
a lot of time during development, making it very easy to test your models
and get a feel for whether you have the right data.
"""


from django.contrib import admin
from .models import Profile


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["user", "timestamp", "bio", "profession"]
    list_filter = ["timestamp"]

    class Meta:
        model = Profile


admin.site.register(Profile, PostModelAdmin)

