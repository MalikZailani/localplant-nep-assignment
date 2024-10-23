from django.contrib import admin
from .models import Profile
# Register your models here.
from .models import Image

admin.site.register(Image)

admin.site.register(Profile)