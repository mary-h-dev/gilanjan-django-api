from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "بدون عنوان"
