from django.urls import path
from .views import *
from . import views

app_name = 'api'

urlpatterns = [
    path('v1/solicitud', Solicitud_APIView.as_view()), 
    path('solicitudes_transporte/', views.lista_solicitudes_transporte, name='lista_solicitudes_transporte'),
    path('solicitudes_transporte/<int:id>/', views.detalle_solicitud_transporte, name='detalle_solicitud_transporte'),
]