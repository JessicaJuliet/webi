# Generated by Django 3.2.6 on 2021-09-02 20:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_content_1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_content_2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_content_3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_subheading_1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_subheading_2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_subheading_3',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(default='Blog content goes here'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
