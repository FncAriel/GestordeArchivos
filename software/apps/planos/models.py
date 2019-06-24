from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class jefeDeTaller(models.Model) :
    u = models.OneToOneField(
        User,
        db_column="user_id",
        unique=True,
        primary_key=True,
        on_delete=models.CASCADE
    )
    telefono = models.BigIntegerField()


class cliente(models.Model) :
    u = models.OneToOneField(
        User,
        db_column="user_id",
        unique=True,
        primary_key=True,
        on_delete=models.CASCADE
    )
    telefono = models.BigIntegerField()
    inmobiliaria = models.TextField()

class arquitecto(models.Model) :
    first_name = models.CharField(max_length=30, default = "")
    last_name = models.CharField(max_length=150, default = "")
    email = models.EmailField(primary_key= True, default = "")
    telefono = models.BigIntegerField(default = "0")
    inmobiliaria = models.CharField(max_length=30, default = "")

      # JSon con las inmobiliarias porque no es modelo

class modelador(models.Model) :
    first_name = models.CharField(max_length=30, default = "")
    last_name = models.CharField(max_length=150, default = "")
    email = models.EmailField(primary_key = True, default = "")
    telefono = models.BigIntegerField(default = "0")
    activo = models.BooleanField()
    jefe = models.ForeignKey(
        jefeDeTaller,
        on_delete=models.SET_NULL,
        null=True
    )


class proyecto(models.Model) :
    inmobiliaria = models.TextField(null=True)
    proyecto_inmobiliario = models.TextField(null=True)
    entrega_total = models.DateField()


#Clase: Entrega Parcial
class hito(models.Model) :
    fecha = models.DateField()
    producto = models.TextField(null=True)  # No me gusta esta forma de lidiar con los productos...
    proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE, null=True)


class plano(models.Model) :
    archivo = models.FileField(upload_to='documents/%Y/%m/%d/')
    especificacion = models.TextField(null=True)
    ultima_carga = models.DateField(auto_now_add=True)
    arquitecto = models.OneToOneField(
        arquitecto,
        on_delete=models.SET_NULL,
        null=True
    )


#Clase: Formulario de Planos
class referencia(models.Model) :
    archivo = models.FileField()
    especificacion = models.FileField()
    plano = models.ForeignKey(plano, on_delete=models.SET_NULL, null=True)
    detalle = models.TextField()


class render(models.Model) :
    proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE)
    archivo = models.FileField()
    finalizado = models.BooleanField(default=False)
    plano = models.OneToOneField(
        plano,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
    )


class revision(models.Model) :
    iteracion = models.SmallIntegerField()
    render = models.OneToOneField(render, on_delete=models.CASCADE)


class anotacion(models.Model) :
    x = models.SmallIntegerField()
    y = models.SmallIntegerField()
    detalle = models.TextField()


class horasHombre(models.Model) :
    inicio = models.DateField()
    termino = models.DateField()
    productos = models.TextField()
    modelador = models.OneToOneField(modelador, on_delete=models.CASCADE)
