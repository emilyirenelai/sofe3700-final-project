# in admin.py
import os
from django.core.wsgi import get_wsgi_application

# Set the path to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mindfullapp.Mindfullapp.settings')

# Initialize the Django application
application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application
from django.contrib import admin
from django.apps import apps

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', r'Mindfullapp.settings')
application = get_wsgi_application()

# Import all models from the 'Mindfullapp' app
app_models = apps.get_app_config('Mindfullapp').get_models()

# Register all models in the admin site
for model in app_models:
    admin.site.register(model)

from django.contrib import admin
from .models import User, JLibrary, Journal, Emotion

admin.site.register(User)
admin.site.register(JLibrary)
admin.site.register(Journal)
admin.site.register(Emotion)

