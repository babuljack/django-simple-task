import os
from .routing import ws_urls
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Task.settings')

application=ProtocolTypeRouter({

   'http':get_asgi_application(),
   'websocket':URLRouter(
         ws_urls
)


}) 

