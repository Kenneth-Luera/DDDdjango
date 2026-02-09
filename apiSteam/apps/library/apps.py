from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apiSteam.apps.library'
    label = 'libraries' 
    
    def ready(self):
        import apiSteam.apps.library.signals