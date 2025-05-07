from django.db import models

class UrlMonitor(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=32, blank=True, null=True)
    has_changed = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    last_checked = models.DateTimeField(blank=True, null=True)

class BoletinUrl(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=32, blank=True, null=True)
    has_changed = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    last_checked = models.DateTimeField(blank=True, null=True)