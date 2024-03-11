from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = user.name
    def __str__(self):
        return str(self.name)

class Animal(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    dateOfBirth = models.DateField()
    sex = models.BooleanField(default=False) #False male, true female
    # Rasse, größe, gewicht, etc
    def __str__(self):
        return str(self.name)