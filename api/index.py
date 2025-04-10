# api/index.py
import os
import sys

from django.core.asgi import get_asgi_application

# Set up Django project path and settings
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager.settings')  # Change if needed

app = get_asgi_application()
