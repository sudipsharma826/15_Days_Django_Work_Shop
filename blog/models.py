from django.db import models
from django.contrib.auth.models import AbstractUser

# Creating the table in the database using AbstractUser Model 
class CustomUser(AbstractUser):
    user_pic = models.ImageField(upload_to='images', null=True, blank=True)
    bio= models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'cms_users'  # This sets the table name to 'cms_users'

    def __str__(self):
        return self.username
    


class Blogs(models.Model):
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

