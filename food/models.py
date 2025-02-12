from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import uuid
from tag.models import Tag  
from django_ckeditor_5.fields import CKEditor5Field

User = settings.AUTH_USER_MODEL





class FoodCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('دسته‌بندی غذا'))

    class Meta:
        verbose_name = _('دسته‌بندی غذا')
        verbose_name_plural = _('دسته‌بندی‌های غذا')

    def __str__(self):
        return self.name





class Food(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('شناسه')
    )
    category = models.ForeignKey(
        FoodCategory, on_delete=models.SET_NULL, null=True, verbose_name=_('دسته‌بندی')
    )
    name = models.CharField(max_length=255, verbose_name=_('نام غذا'))
    slug = models.SlugField(
        max_length=255, unique=True, allow_unicode=True, verbose_name=_('اسلاگ')
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('نویسنده')
    )
    ingredients = CKEditor5Field(
        'مواد اولیه', config_name='default' 
    )

    recipe = CKEditor5Field(
        'دستور پخت', config_name='default' 
    )
    image = models.ImageField(
        upload_to='uploads/foods/%Y/%m/%d', blank=True, null=True, verbose_name=_('تصویر غذا')
    )
    is_active = models.BooleanField(
        default=True, verbose_name=_('فعال/غیرفعال')
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_('تاریخ به‌روزرسانی'))
    # اضافه کردن فیلدهای view_count و tags در صورت نیاز
    view_count = models.PositiveIntegerField(default=0, verbose_name=_('تعداد بازدید'))
    tags = models.ManyToManyField(
        Tag, related_name='foods', verbose_name=_('تگ‌ها')
    )

    class Meta:
        verbose_name = _('غذا')
        verbose_name_plural = _('غذاها')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Food, self).save(*args, **kwargs)





# اضافه کردن مدل FoodSection
class FoodSection(models.Model):
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='sections', verbose_name=_('غذا')
    )
    title = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('عنوان بخش')
    )
    image = models.ImageField(
        upload_to='uploads/foods/sections/%Y/%m/%d', blank=True, null=True, verbose_name=_('تصویر بخش')
    )
    description = CKEditor5Field(
        'توضیحات بخش',blank=True, null=True,  config_name='default'
    )
    order = models.PositiveIntegerField(default=0, verbose_name=_('ترتیب'))

    class Meta:
        ordering = ['order']
        verbose_name = _('بخش غذا')
        verbose_name_plural = _('بخش‌های غذا')

    def __str__(self):
        return f"{self.title} - {self.food.name}"





class FoodLike(models.Model):
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='likes', verbose_name=_('غذا')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('کاربر')
    )
    liked = models.BooleanField(
        default=True, verbose_name=_('پسندیدن')
    )

    class Meta:
        verbose_name = _('پسندیدن غذا')
        verbose_name_plural = _('پسندیدن‌های غذا')
        unique_together = ('food', 'user')

    def __str__(self):
        return f"{self.user.username} پسندیده {self.food.name}"




class FoodComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('کاربر')
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='comments', verbose_name=_('غذا')
    )
    text = models.TextField(verbose_name=_('متن نظر'))
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
        verbose_name = _("نظر درباره غذا")
        verbose_name_plural = _("نظرات درباره غذاها")

    def __str__(self):
        return f"نظر توسط {self.user.username} روی {self.food.name}"
