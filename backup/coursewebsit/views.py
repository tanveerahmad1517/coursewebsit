
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from courses.models import Course

from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from coursewebsit.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from courses.models import PointOfInterest

def poi_list(request):
    pois = PointOfInterest.objects.all()
    return render(request, 'poi_list.html', {'pois': pois})


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

# def myprofileview(request, username):
#     user = User.objects.get(user = request.user)
#     return rende(request,'profile.html',{'user':user})
    

def contact(request):
    form_class = ContactForm
    pois = PointOfInterest.objects.all()

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['tanveerobjects@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('success')

    return render(request, 'contactus.html', {
        'form': form_class, 'pois': pois
    })

def successView(request):
    return render(request, 'success.html')




