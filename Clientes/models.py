from django.utils import timezone
from django.utils.timezone import datetime
from django.db import models
from datetime import date
from datetime import datetime

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
	patente = models.ImageField(upload_to='images/')
	tipo = models.CharField(choices = TIPO, max_length = 50)

	def __str__(self):
		return 'Cliente: ' + self.nombre


		
			
class suscripcion(models.Model):
	estado = models.CharField(max_length=50)
	fecha_expiracion = models.DateField(auto_now_add = False)
	fecha_creacion = models.DateField(auto_now_add = True)
	cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
	precio = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	

	def __str__(self):
		return 'Suscripcion: ' + self.estado


	def function(self):
		self.estado = 'prueba'
		return self.estado











	
	
