from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView

from .forms import SignUpForm


class SubmittableLoginView(LoginView):
    template_name = 'login_form.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'login_form.html'


class SignUpView(CreateView):
    template_name = 'login_form.html'
    form_class = SignUpForm

