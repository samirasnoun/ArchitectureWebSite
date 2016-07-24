# -*- coding: utf8 -*-
"""
WSGI config for archi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""



# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "archi.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# from dj_static import Cling

# application = Cling(get_wsgi_application())



import sys
import os
import os.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'archi')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archi.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
