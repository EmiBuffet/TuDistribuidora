from django.contrib import admin

from distribuidora.models import Pedido
from distribuidora.models import Categoria
from distribuidora.models import Producto
from distribuidora.models import DetallePedido

admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetallePedido)
