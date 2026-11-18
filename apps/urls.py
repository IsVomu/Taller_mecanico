from django.urls import path
from .views import RepuestoListView, RepuestoDetailView, RepuestoCreateView, RepuestoUpdateView, RepuestoDeleteView

urlpatterns = [
    path('', RepuestoListView.as_view(), name='repuesto_list'),
    path('repuesto/<int:pk>/', RepuestoDetailView.as_view(), name='repuesto_detail'),
    path('repuesto/nuevo/', RepuestoCreateView.as_view(), name='repuesto_create'),
    path('repuesto/<int:pk>/editar/', RepuestoUpdateView.as_view(), name='repuesto_update'),
    path('repuesto/<int:pk>/eliminar/', RepuestoDeleteView.as_view(), name='repuesto_delete'),
]