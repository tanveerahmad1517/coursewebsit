
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from courses.models import Course

from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs = Course.objects.filter(
                    Q(title__icontains=query)
                )
        context = {"courses": qs}
        return render(request, "search.html", context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def myprofileview(request, username):
    user = User.objects.get(user = request.user)
    return render(request,'profile.html',{'user':user})
            
