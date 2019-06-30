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
    image_caption = HTMLField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.CharField(max_length =50)
    comments = models.CharField(max_length =50)
    
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

    '''search by image_name'''
    @classmethod
    def search_by_username(cls, search_term):
        posts = cls.objects.filter(username__icontains=search_term)
        return posts
    class Meta:
        ordering=["-id"]        