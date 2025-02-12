from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=500,unique=True,verbose_name="نام تگ")
    eng_title = models.CharField(max_length=500,unique=True,verbose_name="نام تگ به انگلیسی",blank=True)
    def __str__(self):
        return self.name