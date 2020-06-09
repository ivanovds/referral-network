import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Handles signal of user creating.

    When user is created, this function:
    1) generates an unique referral code
    2) creates profile for current user with unique referral code
    """
    if created:
        ref_code = generate_ref_code()
        while Profile.objects.filter(ref_code=ref_code).exists():
            ref_code = generate_ref_code()

        Profile.objects.create(
            user=instance,
            ref_code=ref_code,
        )
    instance.profile.save()


def generate_ref_code(ref_code_length=15):
    """Generates an unique referral code which contains digits and lowercase letters."""
    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(ref_code_length))
