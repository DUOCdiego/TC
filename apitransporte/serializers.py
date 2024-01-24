from rest_framework import serializers
from transporte.models import SolicitudTransporte


      
class SolicitudesTransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudTransporte
        fields = 'all'
 