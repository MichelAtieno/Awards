from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to ='prof_pictures/')
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="")

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def get_profile(cls,id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls,id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def search_profile(cls,id):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile



class Image(models.Model):
    photo = models.ImageField(upload_to ='prof_pictures/')
    project_name = models.CharField(max_length = 100)
    project_caption =  models.CharField(max_length = 100)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    

    @classmethod
    def get_image(cls, id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_profile_image(cls,profile):
        images = Image.objects.filter(user_profile__pk=profile)
        return images

