# Generated by Django 3.1.6 on 2021-02-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0008_auto_20210211_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]