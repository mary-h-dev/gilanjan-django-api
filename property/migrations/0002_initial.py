# Generated by Django 5.0.2 on 2024-11-22 04:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("property", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="favorited",
            field=models.ManyToManyField(
                blank=True,
                related_name="favorites",
                to=settings.AUTH_USER_MODEL,
                verbose_name="علاقه\u200cمندی\u200cها",
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="landlord",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="properties",
                to=settings.AUTH_USER_MODEL,
                verbose_name="مالک",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to=settings.AUTH_USER_MODEL,
                verbose_name="ایجاد کننده",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="property",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to="property.property",
                verbose_name="ملک",
            ),
        ),
    ]
