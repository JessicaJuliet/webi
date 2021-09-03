# Generated by Django 3.2.6 on 2021-09-03 13:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210902_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image_url',
            new_name='blog_image_url',
        ),
        migrations.AddField(
            model_name='blog',
            name='heading',
            field=models.CharField(default='Heading', max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(default='Blog content'),
        ),
    ]
