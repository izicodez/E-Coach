from django.urls import path

from ECoachApp.consumers import WSConsumer

ws_urlpatterns = [
    path('<list_id>/start/ws/', WSConsumer.as_asgi())
]