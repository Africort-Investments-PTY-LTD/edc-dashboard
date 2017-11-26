from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

name = f'edc_dashboard.middleware.DashboardMiddleware'
if name not in settings.MIDDLEWARE:
    raise ImproperlyConfigured(f'Missing middleware. Expected {name}.')
