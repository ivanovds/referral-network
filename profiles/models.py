"""Post Models

A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""


from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_location(instance, filename):
    return '/'.join(['profiles', str(instance.user.id), filename])


class Profile(models.Model):
    STUDENT = 'ST'
    PROGRAMMER = 'PR'
    ENGINEER = 'EN'
    ML_ENGINEER = 'ML'
    OTHER = 'OR'
    PROFESSION_CHOICES = [
        (STUDENT, 'Student'),
        (PROGRAMMER, 'Programmer'),
        (ENGINEER, 'Engineer'),
        (ML_ENGINEER, 'Machine Learning engineer'),
        (OTHER, 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    profession = models.CharField(
        max_length=2,
        choices=PROFESSION_CHOICES,
        null=True,
        blank=True
    )
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field",
                              default='default_img.png',
                              )
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    def get_absolute_url(self):
        return "/profiles/%i/" % self.id

    def __str__(self):
        return self.bio

    class Meta:
        ordering = ["-timestamp"]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
