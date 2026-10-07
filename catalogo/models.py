from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    imagen = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class Compra(models.Model):
    consumidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    producto = models.ForeignKey(
        Producto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='compras',
    )
    nombre_producto = models.CharField(max_length=100)
    precio_unitario = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_producto} x {self.cantidad} ({self.consumidor.username})"