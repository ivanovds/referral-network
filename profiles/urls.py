"""Posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from profiles.views import (
    profile_list,
    profile_detail,
    login_register_view,
    logout_view,
    home_view,
    )


urlpatterns = [
    path('', login_register_view, name='login-register'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('profiles/', profile_list, name='list'),
    path('profiles/<int:profile_id>/', profile_detail, name='detail'),
]
