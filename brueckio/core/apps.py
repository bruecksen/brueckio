from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'brueckio.core'
    verbose_name = "Core"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import core.signals  # noqa F401
        except ImportError:
            pass
