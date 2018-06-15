from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
import misaka
import os
def get_image_path(instance, filename):
    return os.path.join('course_image', str(instance.title), filename)

class Course(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    title_html = models.TextField(editable=False)
    description = models.TextField()
    teacher = models.ForeignKey('Teacher',  related_name='teahcers', on_delete=models.CASCADE, default='Select Teacher')
    image = models.ImageField(upload_to=get_image_path, default='media/default.png')
    def save(self, *args, **kwargs):
        self.title_html = misaka.html(self.title)
        super().save(*args, **kwargs)
  
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse(
            "courses:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]

class Step(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    related_created_at = models.DateTimeField(auto_now=True)
    related_title = models.TextField()
    related_title_html = models.TextField(editable=False)
    related_description = models.TextField()
    related_teacher = models.ForeignKey('Teacher',  related_name='related_teahcers', on_delete=models.CASCADE)
    related_image = models.ImageField(upload_to="Step_Images", default='media/default.png')
    order = models.IntegerField(blank=True, default=0)
    def get_absolute_url(self):
        return reverse("courses:course_detail", args=[str(self.course.pk)])
    def __str__(self):
        return self.related_title

class Teacher(models.Model):
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=30, blank=True)
    github = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
