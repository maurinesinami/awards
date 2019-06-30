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