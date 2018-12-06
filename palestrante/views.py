from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

@login_required
def palestrante(request):
    return render(request, 'palestrante.html')



class AutenticaCad(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

# ----------------------  LIST    ----------------------------

class palestranteList(AutenticaCad, ListView):
    model = Palestrante
    template_name = 'palestrante/palestrante_list.html'
    context_object_name = 'palestrantes'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('pesquisa', None)
        if q :
            palestrantes = Palestrante.objects.filter(palestrante__icontains=q) |\
                           Palestrante.objects.filter(tema__icontains=q)
            return palestrantes
        else:
            palestrantes = Palestrante.objects.all()
            return palestrantes




# ----------------------  CREATE  ----------------------------

class palestranteCreate(AutenticaCad, CreateView):
    model = Palestrante
    fields = ['tema', 'palestrante', 'cargo', 'resumo', 'email', 'telefone', ]
    template_name = 'palestrante/palestrante_create.html'
    success_url = reverse_lazy('palestrante_list')

# ----------------------  DETAIL  ----------------------------

class palestranteDetail(AutenticaCad, DetailView):
    model = Palestrante


# ----------------------  UPDATE  ----------------------------

class palestranteUpdate(AutenticaCad, UpdateView):
    model = Palestrante
    fields = ['tema', 'palestrante', 'cargo', 'resumo', 'email', 'telefone', ]
    template_name = 'palestrante/palestrante_update.html'
    success_url = reverse_lazy('palestrante_list')

# ----------------------  DELETE  ----------------------------

class palestranteDelete(AutenticaCad, DeleteView):
    model = Palestrante
    template_name = 'palestrante/palestrante_delete.html'
    success_url = reverse_lazy('palestrante_list')