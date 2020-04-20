from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer (serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vehiculo
		fields = ('marca', 'modelo', 'linea', 'codigo_universal')