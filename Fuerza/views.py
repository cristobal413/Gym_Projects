from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ProductoGym, Categoria
from .forms import ProductoGymForm


class ProductoListView(ListView):
    model = ProductoGym
    template_name = 'Fuerza/producto_list.html'
    context_object_name = 'productos'
    paginate_by = 8

    def get_queryset(self):
        queryset = ProductoGym.objects.select_related('categoria').all()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['categoria_seleccionada'] = self.request.GET.get('categoria', '')
        return context


class ProductoDetailView(DetailView):
    model = ProductoGym
    template_name = 'Fuerza/producto_detail.html'
    context_object_name = 'producto'


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = ProductoGym
    form_class = ProductoGymForm
    template_name = 'Fuerza/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, '¡Artículo agregado al catálogo correctamente!')
        return super().form_valid(form)


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductoGym
    form_class = ProductoGymForm
    template_name = 'Fuerza/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.success(self.request, '¡Artículo actualizado correctamente!')
        return super().form_valid(form)


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductoGym
    template_name = 'Fuerza/producto_confirm_delete.html'
    context_object_name = 'producto'
    success_url = reverse_lazy('producto_list')

    def form_valid(self, form):
        messages.warning(self.request, 'El artículo fue eliminado del catálogo.')
        return super().form_valid(form)