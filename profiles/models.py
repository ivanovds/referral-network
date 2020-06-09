"""Post Models

A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""

from django.db import models
from django.contrib.auth.models import User


def upload_avatar(instance, filename):
    """Returns path to avatar in media directory."""
    return '/'.join(['profiles', str(instance.user.id), filename])


class Profile(models.Model):
    """User profile.

    Using one-to-one communication with a user model.
    Stores additional user information.
    Stores only current avatar.
    """
    BLANK = ''
    STUDENT = 'ST'
    PROGRAMMER = 'PR'
    ENGINEER = 'EN'
    ML_ENGINEER = 'ML'
    OTHER = 'OR'
    PROFESSION_CHOICES = [
        (BLANK, 'Your profession?'),
        (STUDENT, 'Student'),
        (PROGRAMMER, 'Programmer'),
        (ENGINEER, 'Engineer'),
        (ML_ENGINEER, 'Machine Learning engineer'),
        (OTHER, 'Other'),
    ]
    profession = models.CharField(
        max_length=2,
        choices=PROFESSION_CHOICES,
        null=True,
        blank=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    avatar = models.ImageField(upload_to=upload_avatar,
                               null=False, blank=False,
                               default='default_avatar.png',
                               )
    bio = models.CharField(max_length=500, blank=True)
    ref_code = models.TextField(max_length=20, null=False, unique=True)

    def get_absolute_url(self):
        return "/profiles/%i/" % self.id

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-timestamp"]


def upload_profile_images(instance, filename):
    """Returns path to profile image in media directory."""
    return '/'.join(['profiles', str(instance.profile.user.id), filename])


class ProfileImage(models.Model):
    """Stores not only current avatar but all added avatars."""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_images")
    image = models.ImageField(upload_to=upload_profile_images,
                              null=True, blank=True,
                              )
