# Generated by Django 3.0.3 on 2020-02-29 21:49

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
