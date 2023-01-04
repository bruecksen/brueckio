from django.db import models
from wagtail.contrib.settings.models import (
    BaseSiteSetting,
    register_setting,
)
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


@register_setting
class SiteSpecificSocialMediaSettings(BaseSiteSetting):
    xing = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()

    class Meta:
        verbose_name = 'Social Media Settings'

@register_setting
class SiteSpecificJSSettings(BaseSiteSetting):
    google_analytics = models.TextField()


    class Meta:
        verbose_name = 'JS Settings'