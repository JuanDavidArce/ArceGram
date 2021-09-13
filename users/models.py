"""Users models"""
#Django
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model

import posts.models as post_models
# Create your models here.
class Profile(models.Model):
    """Profile model that extends the base date with other information"""
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    website=models.URLField(max_length=200,blank=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)
    picture= models.ImageField(upload_to='users/pictures',blank=True)

    created= models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    @property
    def followed_by(self):
        return [foll.follower_id for foll in Follower.objects.filter(user_id=self.user.pk)]
    @property
    def following_to(self):
        return [foll.user_id for foll in Follower.objects.filter(follower_id=self.user.pk)]

    @property
    def published(self):
        return len([post for post in post_models.Post.objects.filter(user_id=self.user.pk)])


    def __str__(self) :
        """return username"""
        return self.user.username


class Follower(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Users")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    follower = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Followers")

