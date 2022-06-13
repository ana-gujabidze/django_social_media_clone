from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from accounts import forms


class SingUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")
