"""posts models"""

#IMPORTANT: BY DEFAULT DJANGO ADD AN ID IN OUR TABLES
#in this part classes in our database are gonna be the tables

#Django
from users.models import Profile
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    """Post model"""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    title=models.CharField(max_length= 255)
    photo=models.ImageField(upload_to='posts/photos')

    created =models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)

    likes=models.IntegerField(default=0)

    def __str__(self) :
        """Return title and username"""
        return '{} by @{}'.format(self.title,self.user.username)