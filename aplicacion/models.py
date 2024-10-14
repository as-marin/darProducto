from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):

    TIPOS_DE_PRODUCTO = [
        ('Carniceria', 'Carniceria'),
        ('Bebidas', 'Bebidas'),
        ('Despensa', 'Despensa'),
        ('Lacteos', 'Lacteos'),
        ('Limpieza', 'Limpieza'),
        ('Frutas y Verduras', 'Frutas y Verduras'),
    ]



    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    precio=models.IntegerField(null=False)
    descripcion=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='productos',null=False)
    tipo = models.CharField(max_length=20, choices=TIPOS_DE_PRODUCTO, default='despensa')
    

    def __str__ (self):
        return f"{self.id} - {self.nombre}"


# carrito ---------------------------------------------------------------------------------
class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def total_carrito(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Carrito de {self.usuario}"
    
    
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"Item del carrito de {self.carrito.usuario.nombre}: {self.producto.nombre}"



class Pedido(models.Model):
    EN_PROCESO = 'En Proceso'
    FINALIZADO = 'Finalizado'

    ESTADO_CHOICES = [
        (EN_PROCESO, 'En Proceso'),
        (FINALIZADO, 'Finalizado'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.TextField()  
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    nombre_completo = models.CharField(max_length=255)
    email = models.EmailField()
    direccion = models.TextField()
    departamento_oficina_piso = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default=EN_PROCESO)

    def __str__(self):
        return f"Pedido de {self.usuario.nombre} - {self.fecha_pedido}"


# class DetallePedido(models.Model):
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.PositiveIntegerField(default=1)
#     precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

#     def subtotal(self):
#         return self.cantidad * self.precio_unitario

#     def __str__(self):
#         return f"Detalle de {self.producto.nombre} - Cantidad: {self.cantidad}"



class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser ingresado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
    def create_staff_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True,primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'nombre', 'apellido', 'telefono', 'fecha_nacimiento']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


