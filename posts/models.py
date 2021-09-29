"""posts models"""

#IMPORTANT: BY DEFAULT DJANGO ADD AN ID IN OUR TABLES
#in this part classes in our database are gonna be the tables

#Django
from django.db.models.deletion import CASCADE
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

    description= models.TextField(default="")

    @property
    def liked_by(self):
        return [like.user_id for like in Like.objects.filter(post_id=self.pk)]
    
    @property
    def comments(self):
        return Comment.objects.filter(post_id=self.pk)

    def __str__(self) :
        """Return title and username"""
        return '{} by @{}'.format(self.title,self.user.username)



class Like(models.Model):
    """Like model"""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)


class Comment(models.Model):
    """Coment model"""
    comment= models.TextField()
    user = models.ForeignKey(User,on_delete=CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    created =models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)


