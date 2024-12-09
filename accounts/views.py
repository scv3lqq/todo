from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
