from django.apps import AppConfig

class StudentportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studentportal'
    verbose_name = 'STUDENTPORTAL'

    def ready(self):
        import studentportal.signals  # signals register කරන කොටස
