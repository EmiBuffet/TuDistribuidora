from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer


def home(request):
    return render(request, 'home.html', {'meta_title': 'Home'})


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hola, Somos Tu Distribuidora!'}
        return Response(content)


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #Agregar validacion para cuando quieren Eliminar, si tiene productos cargados con esta.


class ProductoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


