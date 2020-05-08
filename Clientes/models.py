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
	patente = models.ImageField(upload_to='images/')
	tipo = models.CharField(choices = TIPO, max_length = 50)

	def __str__(self):
		return 'Cliente: ' + self.nombre


		
			
class suscripcion(models.Model):
	ESTADO = (
		('activa', 'Activa'),
		('inactiva', 'Inactiva'),
		)	
	estado = models.CharField(choices = ESTADO, max_length=50)
	fecha_expiracion = models.DateField()
	fecha_creacion = models.DateField()
	cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
	

	def __str__(self):
		return 'Suscripcion: ' + self.estado

	menostaller = 0.10
	menosmayorista = 0.25

	
	
