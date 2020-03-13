from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100,blank=true)

    def __str__(self):
        return self.description

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profpics')
    bio = models.TextField(blank = True)
    user_id = models.OneToOneField(user, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_user(self):
        self.save()

    @receiver(post_save,sender=User)
    def create_user_Profile(sender,instance)