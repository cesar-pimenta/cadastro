from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

@login_required
def home(request):
    return render(request, 'home.html')

class AutenticaHome(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

# ----------------------  LIST    ----------------------------

# ----------------------  UPDATE  ----------------------------
