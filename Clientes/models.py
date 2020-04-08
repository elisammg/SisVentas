from django.utils import timezone
from django.db import models

# Create your models here.



class cliente (models.Model):
	TIPO = (
			('mayorista', 'Mayorista'),
			('taller', 'Taller'),
			('individual', 'Individual'),
		)

	nit = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	telefono = models.IntegerField(verbose_name='Telefono')
	patente = models.CharField(max_length=60)
	tipo = models.CharField(choices = TIPO, max_length = 50)
	def unicode (self):
		return self.nombre
		
			
class suscripcion(models.Model):
	ESTADO = (
		('activa', 'Activa'),
		('inactiva', 'Inactiva'),
		)	
	estado = models.CharField(choices = ESTADO, max_length=50)
	fecha_expiracion = models.DateField()
	fecha_creacion = models.DateField()
	cliente = models.ForeignKey(cliente, on_delete=models.PROTECT)
	def unicode (self):
		return self.estado
	
	def estadosuscripcion(self):
		hoy = datetime.date.today()
		dias = (self.fecha_expiracion - hoy).days
		return dias