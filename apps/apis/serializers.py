from rest_framework import serializers
from apps.apis.models import Routingorder, Almacen, Persona, Tablageneral


class PersonaShipperSerializable(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'nombre'
        )

class TablaGeneralShipperSerializable(serializers.ModelSerializer):
    class Meta:
        model = Tablageneral
        fields = (
            'descripcion'
        )

class RoutingOrderSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super(RoutingOrderSerializer, self).to_representation(instance)
        persona = Persona.objects.filter(codigopersona__exact=instance.codigoshipper).get()
        data['nombre_shipper'] = persona.nombre

        tabla_general = Tablageneral.objects.filter(tipotabla='CT', codigotabla=instance.tipocondicioncarga).get()
        data['condicioncarga'] = tabla_general.descripcion
        return data

    class Meta:
        model = Routingorder
        fields = (
            'numeroroutingorder',
            'tipooperacion',
            'codigoshipper',
            'codigoejecutivoventa',
            'fechaemision',
            'numeroguiamaster',
            'descripcionmerca',
            'tipocondicioncarga'
        )