from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
import django_filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, status, filters
from .models import Categoria, Producto, Usuario
from .serializers import CategoriaSerializer, ProductoSerializer, UsuarioSerializer


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']
    #Agregar validacion para cuando quieren Eliminar, si tiene productos cargados con esta.


class ProductoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['nombre']
    ordering_fields = ('nombre', 'fecha_carga')


class UsuarioViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = Usuario.objects.filter(username=pk)
        usuario = get_object_or_404(queryset, pk=1)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)


    def update(self, request, pk=None):
        queryset = Usuario.objects.filter(username=pk)
        usuario = get_object_or_404(queryset, pk=1)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


