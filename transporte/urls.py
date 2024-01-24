from django.urls import path, include

from rest_api_bodega.views import lista_solicitudes_transporte
from .views import index
from django.contrib import admin

urlpatterns = [
    # path('transporte/', include('transporte.urls')),
    path('', index, name="transporte_index"),
    path('admin/', admin.site.urls),
    path('solicitudes/', lista_solicitudes_transporte, name='lista_solicitudes_transporte'),
]

