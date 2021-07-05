from django.apps import AppConfig


class StutorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stutor'

    def ready(self):
        import stutor.signals
