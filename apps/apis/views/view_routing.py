from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.apis.models import Routingorder
from apps.apis.serializers import RoutingOrderSerializer


class RoutingOrder(APIView):
    model = Routingorder
    serializer_model = RoutingOrderSerializer

    def post(self, request):
        print(request.data)
        rangofecha_inicial = request.data['fechainicial']
        rangofecha_final = request.data['fechafinal']

        routingorders_obj = self.model.objects.filter(fechaemision__gte=rangofecha_inicial, fechaemision__lte=rangofecha_final).order_by('fechaemision')
        serializer = self.serializer_model(routingorders_obj, many=True)
        data = {
            'message': "Se encontraron resultados.",
            'status': "success",
            'status_code': status.HTTP_200_OK,
            'results': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
