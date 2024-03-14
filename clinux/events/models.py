from django.db import models


class EventSession(models.Model):
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="sessions",
        null=False,
        blank=False,
    )
    start = models.DateTimeField()
    end = models.DateTimeField()


# Create your models here.


class Event(models.Model):
    slug = models.SlugField(unique=True, max_length=100)
    title = models.CharField(null=False, blank=False, max_length=100)
    subtitle = models.CharField(default="", blank=True, max_length=100)
    description = models.TextField(default="", blank=True)

    # TO_DO: timestamp
    # hours = models.CharField()
    # level = models.CharField()
    # image = models.ImageField(upload_to = user_directory_path)
