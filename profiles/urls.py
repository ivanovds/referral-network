"""Profile URL Configuration"""


from django.urls import path
from profiles.views import (
    profile_list,
    profile_detail,
    register_view,
    login_view,
    logout_view,
    my_profile,
    )


urlpatterns = [
    path('', my_profile, name='home'),
    path('signup/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profiles/', profile_list, name='list'),
    path('profiles/<int:profile_id>/', profile_detail, name='detail'),
]
