# Generated by Django 4.0 on 2022-02-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_post_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='live',
            field=models.URLField(blank=True, null=True),
        ),
    ]
