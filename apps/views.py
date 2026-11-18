from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Repuesto
from .forms import RepuestoForm

class RepuestoListView(ListView):
    model = Repuesto
    template_name = 'taller/repuesto_list.html'
    context_object_name = 'repuestos'

    def get_queryset(self):
        # Optimización ORM obligatoria contra N+1 queries
        return super().get_queryset().select_related('categoria')

class RepuestoDetailView(DetailView):
    model = Repuesto
    template_name = 'taller/repuesto_detail.html'
    context_object_name = 'repuesto'

class RepuestoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Repuesto
    form_class = RepuestoForm
    template_name = 'taller/repuesto_form.html'
    success_url = reverse_lazy('repuesto_list')
    success_message = "¡Repuesto registrado exitosamente!"

class RepuestoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Repuesto
    form_class = RepuestoForm
    template_name = 'taller/repuesto_form.html'
    success_url = reverse_lazy('repuesto_list')
    success_message = "¡Repuesto actualizado correctamente!"

class RepuestoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Repuesto
    template_name = 'taller/repuesto_confirm_delete.html'
    success_url = reverse_lazy('repuesto_list')
    success_message = "¡Repuesto eliminado del inventario!"