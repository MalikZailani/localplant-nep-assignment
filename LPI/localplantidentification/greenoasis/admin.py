from django.contrib import admin
from .models import Profile
# Register your models here.
from .models import Image
from .models import Feedback

admin.site.register(Image)

admin.site.register(Profile)

admin.site.register(Feedback)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'message') 