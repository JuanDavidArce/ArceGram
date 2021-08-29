"""posts models"""
#Django
from django.db import models
from django.db.models.fields import CharField
#IMPORTANT: BY DEFAULT DJANGO ADD AN ID IN OUR TABLES
#in this part classes in our database are gonna be the tables
class User(models.Model):
    """User model"""
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio=models.TextField(blank=True)
    birthdate=models.DateField(blank=True,null=True)

    created= models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.email