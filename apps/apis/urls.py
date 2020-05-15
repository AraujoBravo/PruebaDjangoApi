from django.urls import path, re_path
from apps.apis.views.view_routing import RoutingOrder
from django.conf.urls import url

app_name = 'apis'
urlpatterns = [
    url(r'^routingOrder/', RoutingOrder.as_view(), name='routing_order'),
]

