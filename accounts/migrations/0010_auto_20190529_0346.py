# Generated by Django 2.0.7 on 2019-05-28 21:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190529_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]