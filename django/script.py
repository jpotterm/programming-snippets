#!/var/www/site/venv/bin/python

# If script file is not in /var/www/site/src
import sys
sys.path.append('/var/www/site/src')

# Initialize Django
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


print('Hello world')
