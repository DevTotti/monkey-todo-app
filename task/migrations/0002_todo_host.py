# Generated by Django 3.2 on 2021-06-29 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='host',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
    ]
