from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    image = FilerImageField(null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
