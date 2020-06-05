"""Account URL Configuration"""


from django.urls import path
from accounts.views import (
    register_view,
    login_view,
    logout_view,
    )


urlpatterns = [
    path('signup/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
