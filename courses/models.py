from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey

import os
from django.contrib.contenttypes.models import ContentType
class CourseQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()

    def get_related(self, instance):
        courses_one = self.get_queryset().filter(category=instance.category)
        courses_two = self.get_queryset().filter(default=instance.default)
        qs = (courses_one | courses_two).exclude(id=instance.id).distinct()
        return qs


def get_image_path(instance, filename):
    return os.path.join('course_image', str(instance.title), filename)

class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name





class Course(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    title_html = models.TextField(editable=False)
    description = models.TextField()
    teacher = models.ForeignKey('Teacher',  related_name='teahcers', on_delete=models.CASCADE, default='Select Teacher')
    image = models.ImageField(upload_to=get_image_path, default='media/default.png')
    active = models.BooleanField(default=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True,blank=True)
    default = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='default_category', null=True, blank=True)
    slug = models.SlugField()
    objects = CourseManager()
    class Meta:
        ordering = ["-title"]

    def get_related_courses_by_tags(self):
        return Course.objects.filter(tags__in=self.tags.all())
    # @property
    # def comments(self):
    #     instance = self
    #     qs = Comment.objects.filter_by_instance(instance)

    # @property
    # def get_content_type(self):
    #     instance = self 
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type
  
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})


    # class Meta:
    #     ordering = ["-created_at"]

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


