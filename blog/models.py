from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from tag.models import Tag
import uuid
from django_ckeditor_5.fields import CKEditor5Field

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('دسته‌بندی'))

    def __str__(self):
        return self.name



class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('شناسه')
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name=_('دسته‌بندی')
    )
    title = models.CharField(max_length=255, verbose_name=_('عنوان'))
    slug = models.SlugField(
        max_length=255, unique=True, allow_unicode=True, verbose_name=_('اسلاگ')
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('مالک')
    )
    meta_description = models.CharField(
        verbose_name=_("توضیحات متا"), max_length=200, null=True, blank=True
    )
    page_meta = models.CharField(
        verbose_name=_("متای صفحه"), max_length=200, null=True, blank=True
    )
    canonical = models.URLField(
        null=True, blank=True, verbose_name=_("کنونیکال")
    )
    is_active = models.BooleanField(
        default=True, verbose_name=_('فعال/غیر فعال')
    )
    is_validated = models.BooleanField(
        default=True, verbose_name=_('تایید/عدم تایید')
    )
    tags = models.ManyToManyField(
        Tag, related_name='blogs', verbose_name=_('تگ بلاگ')
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('بلاگ')
        verbose_name_plural = _('بلاگ‌ها')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Blog, self).save(*args, **kwargs)





class BlogSection(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='sections', verbose_name=_('بلاگ')
    )
    title = models.CharField(
        max_length=255, verbose_name=_('عنوان بخش')
    )
    image = models.ImageField(
        upload_to='uploads/blogs/%Y/%m/%d', blank=True, null=True, verbose_name=_('تصویر بخش')
    )
    description = CKEditor5Field(
        'توضیحات بخش', config_name='default'  
    )

    order = models.PositiveIntegerField(default=0, verbose_name=_('ترتیب'))


    class Meta:
        ordering = ['order']
        verbose_name = _('بخش بلاگ')
        verbose_name_plural = _('بخش‌های بلاگ')

    def __str__(self):
        return f"{self.title} - {self.blog.title}"





class BlogLike(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='likes', verbose_name=_('بلاگ')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('کاربر')
    )
    liked = models.BooleanField(
        default=True, verbose_name=_('پسندیدن')
    )

    class Meta:
        verbose_name = _('پسندیدن بلاگ')
        verbose_name_plural = _('پسندیدن‌های بلاگ')
        unique_together = ('blog', 'user')

    def __str__(self):
        return f"{self.user.username} liked {self.blog.title}"






class CommentsBlog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('کاربر')
    )
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, verbose_name=_('بلاگ')
    )
    text = models.TextField(verbose_name=_('متن کامنت'))
    is_active = models.BooleanField(
        default=False, verbose_name=_("تایید/عدم تایید")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('تاریخ ایجاد')
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('تاریخ به‌روزرسانی')
    )

    class Meta:
        verbose_name = _("کامنت در مقاله")
        verbose_name_plural = _("کامنت‌های مقالات")

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"
