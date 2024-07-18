# import celery
from .celery import app as celery_app

# added Celery to the Django project and  can now start using it
__all__ = ['celery_app']
