from django import forms

from .models import Course, Teacher


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("title", "description", "teacher", "image")
        model = Course

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

class CommentForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	content = forms.CharField(widget=forms.Textarea)
