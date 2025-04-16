from django.db import models

class NewsItem(models.Model):
    raw_text = models.TextField()
    clean_text = models.TextField(blank=True)
    location_name = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.raw_text[:80] + "..."

    class Meta:
        verbose_name_plural = "Félix Fénéon"


# Create your models here.
