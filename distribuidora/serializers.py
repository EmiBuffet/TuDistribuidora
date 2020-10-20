from .models import Categoria, Producto
from rest_framework import serializers


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
    #categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'codigo_producto', 'categoria', 'nombre', 'descripcion', 'precio_unitario',
                  'imagen', 'stock', 'cantidad_unidades', 'fecha_baja', 'fecha_carga']

    def to_representation(self, instance):
        self.fields['categoria'] = CategoriaSerializer(read_only=True)
        return super().to_representation(instance)