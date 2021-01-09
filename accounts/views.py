from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import datetime

class Index(TemplateView):
    template_name = 'accounts/login.html'

@login_required
def home(request):    
    template_name = 'accounts/home.html'
    date = datetime.datetime.today()
    context = {
        'date' : date
    }

    return render(request,template_name, context)


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')