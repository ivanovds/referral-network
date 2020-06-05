"""Profile URL Configuration"""


from django.urls import path
from profiles.views import (
    profile_list,
    profile_detail,
    my_profile,
    )


urlpatterns = [
    path('', my_profile, name='home'),
    path('profiles/', profile_list, name='list'),
    path('profiles/<int:profile_id>/', profile_detail, name='detail'),
]
