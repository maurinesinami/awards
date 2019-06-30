from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'awards/', blank = True)
    bio=models.CharField(max_length =50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    contact=models.CharField(max_length =50)
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()
class Image(models.Model):
    image = models.ImageField(upload_to = 'landingpage/')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.image_name

    '''return objects on database'''
    @classmethod
    def images_all(cls):
        posts = Image.objects.all()
        return posts

    '''save function'''
    def save_post(self):
        self.save()

    '''delete function'''
    def delete_post(self):
        self.delete()

    
     