# Generated by Django 3.0.3 on 2020-02-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
