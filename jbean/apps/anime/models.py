from django.db import models

__author__ = 'Jeffrey'


class Show(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    air_day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    watching = models.BooleanField(default=False)
    #thumbnail = models.ImageField(null=True, blank=True, upload_to=settings.MEDIA_URL)
