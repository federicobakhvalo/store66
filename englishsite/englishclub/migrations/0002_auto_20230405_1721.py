# Generated by Django 3.1.5 on 2023-04-05 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('englishclub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabularymodel',
            name='userid',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
