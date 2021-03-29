from django.db import models
from proyecto1.settings import MEDIA_URL, STATIC_URL


from django.contrib.auth.models import User

# tabla 1 a 1 con User
class Cliente(models.Model):
    INTERES  = (('M', 'Hombre'), ('F', 'Mujer'), ('T', 'Todo'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tarjeta = models.CharField(max_length=255, verbose_name="Tarjeta de credito")
    preferencia = models.CharField(max_length=1, choices=INTERES ,verbose_name="Qué te interesa más")

    def __str__(self):
        return str(self.user.username)

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=255, verbose_name="Nombre de la categoria")

    def __str__(self):
        return str(self.nombre_categoria)

class Color(models.Model):
    nombre_color = models.CharField(max_length=255, verbose_name="Nombre del color")

    def __str__(self):
        return str(self.nombre_color)

class Producto(models.Model):
    SEX_OPTIONS  = (('M', 'Hombre'), ('F', 'Mujer'))
    TALLA_OPTIONS = ((1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL'), (5, 'XXL'))
    
    nombre= models.CharField(max_length=255)
    unidades= models.IntegerField()
    precio= models.FloatField()
    desquento_procentaje=models.IntegerField()
    categoria= models.ForeignKey(Categoria, related_name='dishes', on_delete=models.CASCADE)
    talla= models.PositiveSmallIntegerField( default=2, choices=TALLA_OPTIONS)
    sexo= models.CharField(max_length=1, choices=SEX_OPTIONS)
    color= models.ForeignKey(Color, null=True, related_name='dishes', on_delete=models.CASCADE)
    ruta_img=models.FileField()

    def get_img(self):
        if self.ruta_img:
            return '{}{}'.format(MEDIA_URL,self.ruta_img)
        else:
            return '{}{}'.format(STATIC_URL,'/img/modelo.png')


class Compra(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id_produc = models.ForeignKey(Producto, related_name='dishes', on_delete=models.CASCADE)
    precio_desquento = models.FloatField()

    def get_copra(self):
        talla_print=''
        if self.id_produc.talla == 1:
            talla_print='S'
        elif  self.id_produc.talla == 2:
            talla_print='M'
        elif self.id_produc.talla == 3:
            talla_print='L'
        elif  self.id_produc.talla == 4:
            talla_print='XL'
        elif  self.id_produc.talla == 5:
            talla_print='XXL'
        sexo_print=''
        if self.id_produc.sexo == 'M':
            sexo_print='Hombre'
        elif  self.id_produc.sexo == 'F':
            sexo_print='Mujer'
        
        return 'Nombre Producto: '+self.id_produc.nombre+' Talla: '+talla_print+' Sexo: '+sexo_print+' Categoria: '+self.id_produc.categoria.nombre_categoria+' Precio con desquento: '+str(self.precio_desquento)+' €. '
    
    
