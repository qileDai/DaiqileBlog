from django.test import TestCase
from login import models
import requests
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myblog.settings")# project_name 项目名称
django.setup()

# Create your tests here.

response = requests.get('http://127.0.0.1:8000/login/register/')
print(response.text)