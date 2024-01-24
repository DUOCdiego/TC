from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.parsers import JSONParser

from bodega.models import Producto
from .serializers import ProductoSerializer, SolicitudSerializer

from rest_framework import serializers
from bodega.models import Producto

from transporte.models import SolicitudTransporte
from .serializers import SolicitudesTransporteSerializer


@api_view(['GET', 'POST'])

def lista_solicitudes_transporte(request):
    if request.method == 'GET':
        solicitudes = SolicitudTransporte.objects.all()
        serializer = SolicitudesTransporteSerializer(solicitudes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SolicitudesTransporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def detalle_solicitud_transporte(request, id):
    solicitud = SolicitudTransporte.objects.get(id=id)

    if request.method == 'GET':
        serializer = SolicitudesTransporteSerializer(solicitud)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SolicitudesTransporteSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)