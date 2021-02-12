# Generated by Django 3.0 on 2021-02-12 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20210212_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='photo.Category'),
        ),
    ]