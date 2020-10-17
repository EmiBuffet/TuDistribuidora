from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


class Pedido(models.Model):
    ESTADOS = (
        ('1', 'Solicitado'),
        ('2', 'Confirmado'),
        ('3', 'Terminado'),
        ('4', 'Cancelado'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=100)
    entregado = models.BooleanField(null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS)
    fecha_baja = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-fecha_pedido']

    def __str__(self):
        return u"%s %s %s" % (self.fecha_pedido, self.direccion, self.user)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo_producto = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    precio_unitario = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    imagen = models.CharField(null=True, blank=True, max_length=400)
    stock = models.IntegerField(null=True, blank=True)
    cantidad_unidades = models.IntegerField(null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    fecha_carga = models.DateField()

    def __str__(self):
        return u"%s %s %s" % (self.codigo_producto, self.descripcion, self.precio_unitario)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_detalle = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    descuento = models.IntegerField(null=True, blank=True)