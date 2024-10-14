from django.contrib import admin
from .models import Producto,Pedido

class AdmProducto(admin.ModelAdmin):
    list_display=['id','nombre','imagen']
    list_editable=['nombre']





# Register your models here.
admin.site.register(Producto, AdmProducto)

admin.site.register(Pedido)
