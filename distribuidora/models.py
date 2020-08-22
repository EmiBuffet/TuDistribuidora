from django.contrib.auth.models import User
from django.db import models


class Pedidos(models.Model):
    ESTADOS = (
        ('1', 'Solicitado'),
        ('2', 'Confirmado'),
        ('3', 'Terminado'),
        ('4', 'Cancelado'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    direccion = models.CharField(max_length=100)
    entregado = models.BooleanField()
    estado = models.CharField(max_length=1, choices=ESTADOS)

    class Meta:
        ordering = ['-fecha_pedido']