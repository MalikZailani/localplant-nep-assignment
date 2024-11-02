from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Feedback(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.email}"
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Image(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    tags=models.TextField()
    image=models.ImageField(upload_to="pic/%y/")
    like_count = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_post', blank=True)
    

    def __str__(self):
        return self.title
    class Meta :
        ordering=('-id',)

    def get_absolute_url(self):
        return reverse('detail_view', args=[self.id])
    


    
