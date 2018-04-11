from django import forms

from .models import Course, Teacher


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("title", "description", "teacher", "image")
        model = Course

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

