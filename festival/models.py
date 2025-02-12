from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

User = settings.AUTH_USER_MODEL

class Festival(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('شناسه')
    )
    title = models.CharField(max_length=255, verbose_name=_('عنوان فستیوال'))
    slug = models.SlugField(
        max_length=255, unique=True, allow_unicode=True, verbose_name=_('اسلاگ')
    )
    description = models.TextField(verbose_name=_('توضیحات'))
    image = models.ImageField(
        upload_to='uploads/festivals/%Y/%m/%d', blank=True, null=True, verbose_name=_('تصویر فستیوال')
    )
    start_date = models.DateField(verbose_name=_('تاریخ شروع'))
    end_date = models.DateField(verbose_name=_('تاریخ پایان'))
    location = models.CharField(max_length=255, verbose_name=_('محل برگزاری'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_('تاریخ به‌روزرسانی'))
    is_active = models.BooleanField(default=True, verbose_name=_('فعال/غیرفعال'))

    class Meta:
        verbose_name = _('فستیوال')
        verbose_name_plural = _('فستیوال‌ها')
        ordering = ['-start_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Festival, self).save(*args, **kwargs)
