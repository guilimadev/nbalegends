import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # Add this import

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='staticfiles')  # Add this line for static files