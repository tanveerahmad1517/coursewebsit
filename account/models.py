from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    get_picture = models.ImageField(upload_to='Profile_pictures', default='user.png', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    @property
    def image_url(self):
        if self.get_picture and hasattr(self.get_picture, 'url'):
            return self.get_picture.url
    def __str__(self):
        return self.user.username

    
    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()

            else:
                return self.user.username

        except Exception:  # pragma: no cover
            return self.user.username

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)
