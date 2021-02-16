# Generated by Django 3.1.6 on 2021-02-10 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coin', '0003_auto_20210130_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imagecoin',
            name='image',
            field=models.ImageField(upload_to='coins'),
        ),
    ]
