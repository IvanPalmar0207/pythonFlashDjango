from django.contrib import admin
from gestionPedidos.models import tb_Clientes,tb_Articulos,tb_Pedidos


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion","email",'telefono')
    search_fields = ["nombre"]

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("nombre","seccion","precio")
    search_fields = ["nombre"]

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numeroPedido","fecha","entregado")
    search_fields = ["numeroPedido"]

admin.site.register(tb_Clientes,ClientesAdmin)
admin.site.register(tb_Articulos,ArticulosAdmin)
admin.site.register(tb_Pedidos,PedidosAdmin)