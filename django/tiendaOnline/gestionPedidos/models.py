from django.db import models

#Modelos para esta aplicacion

class tb_Clientes(models.Model):
    nombre = models.CharField(max_length=70,verbose_name='Nombre del Cliente')
    direccion = models.CharField(max_length=80, verbose_name = 'Direccion del Cliente')
    email = models.EmailField(blank=True,null=True,max_length=254, verbose_name = 'Email del Cliente')
    telefono = models.CharField(max_length=10, verbose_name = 'Telefono del Cliente')
    
    def __str__(self):
        return 'El cliente es: %s \nLa direccion del cliente es: %s \nEl email del cliente es: %s \nEl telefono del cliente es: %s \n\n' % (self.nombre,self.direccion,self.email,self.telefono)
    
    
class tb_Articulos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre del Articulo')
    seccion = models.CharField(max_length=50, verbose_name = 'Seccion del Articulo')
    precio = models.FloatField(verbose_name = 'Precio del Articulo')
    
    def __str__(self):
        return 'El nombre del articulo es: %s \nLa seccion del articulo es: %s \nEl precio del articulo es: %s \n\n' % (self.nombre,self.seccion,self.precio)
    
    
class tb_Pedidos(models.Model):
    numeroPedido = models.IntegerField(verbose_name = 'Numero del Pedido')
    fecha = models.DateField(auto_now=False, auto_now_add=False,verbose_name = 'Fecha del Pedido')
    entregado = models.BooleanField()
    
    def __str__(self):
        return 'El numero de pedido es: %s \nLa fecha del pedido es: %s \n¿El pedido ha sido entregado? R/ %s \n\n' % (self.numeroPedido,self.fecha, self.entregado)
    
    
#Modelos de ejemplo
'''class tb_metodoPago(models.Model):
    tipoMetodo = models.CharField(max_length=50)'''