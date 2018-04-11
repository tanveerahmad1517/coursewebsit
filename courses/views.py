from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from braces.views import SelectRelatedMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Step
from django.shortcuts import render, get_object_or_404
from . import forms

class AllPosts(ListView):
    model = Course
    paginate_by = 6
class UserPosts(ListView):
    model = Course
    paginate_by = 6
    template_name = "courses/user_timeline.html"

    def get_queryset(self):
        try:
            self.course_user = User.objects.prefetch_related("courses").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.course_user.courses.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course_user"] = self.course_user
        return context


class SinglePost(DetailView):
    model = Course


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/course_detail.html'

class StepDetailView(DetailView):
	model = Step 
	template_name = 'courses/step_detail.html'
	def get_object(self):
		step = get_object_or_404(Step, pk=self.kwargs['step_pk'])
		return step

class CreateStep(LoginRequiredMixin, CreateView):
    model = Step
    fields = '__all__'
    template_name = "courses/create_step.html"



class EditView(UpdateView):
	model = Course
	fields = ['title', 'description', 'teacher', 'image']
	template_name = 'courses/edit_course.html'


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = forms.PostForm
    model = Course
    template_name = "courses/create_course.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class DeletePost(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy("courses:course_list")


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Message successfully deleted")
        return super().delete(*args, **kwargs)

class EditView(UpdateView):
    model = Course
    fields = ['title', 'description', 'teacher', 'image']
    template_name = 'courses/edit_course.html'


class EditStep(UpdateView):
    model = Step
    fields = '__all__'
    template_name = 'courses/edit_step.html'
    def get_success_url(self):
        return reverse_lazy('course_detail',kwargs={'pk': self.get_object().id})
class EditStepDetail(UpdateView):
    model = Step
    fields = '__all__'
    template_name = 'courses/edit_step_detail.html'
    def get_object(self):
        step = get_object_or_404(Step, pk=self.kwargs['step_pk'])
        return step
class DeleteStepDetail(DetailView):
    model = Step
    fields = '__all__'
    template_name = 'courses/course_confirm_delete.html'
    def get_object(self):
        step = get_object_or_404(Step, pk=self.kwargs['step_pk'])
        return step


class MyView(AllPosts):
    def get_queryset(self):
        return Course.objects.filter(user=self.request.user.id) \
        .order_by('-created_at')[:20]
        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            return super(MyView, self).dispatch(*args, **kwargs)
