from vercel_python.server import VercelServer
from django.core.asgi import get_asgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manager.settings")

application = get_asgi_application()
handler = VercelServer(application)