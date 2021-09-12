# Generated by Django 3.2.6 on 2021-09-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_bundle_addon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='addon',
        ),
        migrations.AddField(
            model_name='bundle',
            name='addon',
            field=models.ManyToManyField(to='services.Addon'),
        ),
    ]
