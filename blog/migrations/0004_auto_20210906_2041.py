# Generated by Django 3.2.6 on 2021-09-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210903_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='heading',
            field=models.CharField(max_length=200),
        ),
    ]
