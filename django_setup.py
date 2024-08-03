import os
import django

def django_setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","school_schedule.settings")
    django.setup()