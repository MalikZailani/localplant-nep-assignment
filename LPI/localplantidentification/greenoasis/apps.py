from django.apps import AppConfig


class GreenoasisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greenoasis'
    
    def ready(self):
        import greenoasis.signal