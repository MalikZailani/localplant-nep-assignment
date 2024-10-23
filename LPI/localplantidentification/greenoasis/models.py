from django.db import models
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    tags=models.TextField()
    image=models.ImageField(upload_to="pic/%y/")
    

    def __str__(self):
        return self.title
    class Meta :
        ordering=('-id',)

    def get_absolute_url(self):
        return reverse('detail_view', args=[self.id])

    
