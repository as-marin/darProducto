
from django.urls import path,include

from .views import index, cambiadireccion,cerrar_sesion, cambiatarjeta, editarusuario, eliminarusuario,  carrito, despensa,iniciarsesion, contra, crearu, carniceria, frutayv, gestionusuario, historial_user, historialEnvio, index_copy, bebidas, opciones, pago, user, verificacion, verproducto, limpieza, lacteos, gestion_prod, editarproducto, eliminarproducto


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('cambiadireccion/',cambiadireccion,name='cambiadireccion'),
    path('cambiar tarjeta/',cambiatarjeta,name='cambiar tarjeta'),
    path('carrito/',carrito,name='carrito'),
    path('despensa/',despensa,name='despensa'),
    path('contra/',contra,name='contra'),
    path('crearu/',crearu,name='crearu'),
    path('carniceria/',carniceria,name='carniceria'),
    path('frutayv/',frutayv,name='frutayv'),
    path('gestionusuario/',gestionusuario,name='gestionusuario'),
    path('historial_user/',historial_user,name='historial_user'),
    path('historialEnvio/',historialEnvio,name='historialEnvio'),
    path('index_copy/',index_copy,name='index_copy'),
    path('bebidas/',bebidas,name='bebidas'),
    path('opciones/',opciones,name='opciones'),
    path('pago/',pago,name='pago'),
    path('user/',user,name='user'),
    path('verificacion/',verificacion,name='verificacion'),
    path('verproducto/<id>/',verproducto,name='verproducto'),
    path('limpieza/',limpieza,name='limpieza'),
    path('lacteos/',lacteos,name='lacteos'),
    path('gestion_prod/',gestion_prod,name='gestion_prod'),
    path('editarproducto/<id>/',editarproducto,name='editarproducto'),
    path('eliminarproducto/<id>/',eliminarproducto,name='eliminarproducto'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar_sesion'),
    path('login/',iniciarsesion,name='login'),
    path('editarusuario/<id>/',editarusuario,name='editarusuario'),
    path('eliminarusuario/<id>/',eliminarusuario,name='eliminarusuario'),
    
]
#URLS aplicacion


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)