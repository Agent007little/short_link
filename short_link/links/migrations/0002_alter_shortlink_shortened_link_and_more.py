# Generated by Django 5.0 on 2024-01-01 10:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='shortened_link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='shortlink',
            unique_together={('user', 'shortened_link')},
        ),
    ]
