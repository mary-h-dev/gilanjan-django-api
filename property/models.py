import uuid
from django.conf import settings
from django.db import models
from useraccount.models import User


class Property(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name='شناسه'
    )
    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price_per_night = models.IntegerField(verbose_name='قیمت هر شب')
    bedrooms = models.IntegerField(verbose_name='تعداد اتاق خواب')
    buildingsmeter = models.IntegerField(verbose_name='بنا')
    floorareameters = models.IntegerField(verbose_name='زیر بنا')
    guests = models.IntegerField(verbose_name='تعداد مهمان')
    country = models.CharField(max_length=255, verbose_name='کشور')
    country_code = models.CharField(max_length=10, verbose_name='کد کشور')
    category = models.CharField(max_length=255, verbose_name='دسته‌بندی')
    favorited = models.ManyToManyField(
        User, related_name='favorites', blank=True, verbose_name='علاقه‌مندی‌ها'
    )

    image = models.ImageField(upload_to='uploads/properties/%Y/%m/%d', blank=True, null=True, verbose_name='0تصویر')
    image1 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d', blank=True, null=True, verbose_name='1تصویر')
    image2 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d',  blank=True, null=True,verbose_name='2تصویر')
    image3 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d', blank=True, null=True, verbose_name='3تصویر')
    image4 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d', blank=True, null=True, verbose_name='4تصویر')
    image5 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d', blank=True, null=True,verbose_name='5تصویر')
    image6 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d',blank=True, null=True,verbose_name='6تصویر')
    image7 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d',blank=True, null=True,verbose_name='7تصویر')
    image8 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d', blank=True, null=True,verbose_name='8تصویر')
    image9 = models.ImageField(upload_to='uploads/properties/%Y/%m/%d', blank=True, null=True, verbose_name='9تصویر')

    landlord = models.ForeignKey(
        User, related_name='properties', on_delete=models.CASCADE, verbose_name='مالک'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')


    # def image_url(self):
    #     return f'{settings.WEBSITE_URL}{self.image.url}'

    def get_image_urls(self):
        images = []
        for i in range(10):
            field_name = f'image{i}' if i != 0 else 'image'
            image_field = getattr(self, field_name)
            if image_field and hasattr(image_field, 'url'):
                images.append(f'{settings.WEBSITE_URL}{image_field.url}')
        return images




class Reservation(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name='شناسه'
    )
    property = models.ForeignKey(
        Property, related_name='reservations', on_delete=models.CASCADE, verbose_name='ملک'
    )
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان')
    number_of_nights = models.IntegerField(verbose_name='تعداد شب‌ها')
    guests = models.IntegerField(verbose_name='تعداد مهمان‌ها')
    total_price = models.FloatField(verbose_name='قیمت کل')
    created_by = models.ForeignKey(
        User, related_name='reservations', on_delete=models.CASCADE, verbose_name='ایجاد کننده'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
