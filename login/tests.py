from django.test import TestCase
from login import models

# Create your tests here.
user = models.Uesr.objects.filter(name__contains=1)
print(user)