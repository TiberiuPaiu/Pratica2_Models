from django.contrib import admin
from tienda.models import Categoria , Color , Producto ,Cliente ,Compra
# Register your models here.



class ProductosAdmin(admin.ModelAdmin):
    list_display=("nombre","unidades","precio","desquento_procentaje","categoria","talla","sexo","color","ruta_img")
    search_fields=("nombre","categoria","talla","sexo","color")

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Compra)
admin.site.register(Producto ,ProductosAdmin)
