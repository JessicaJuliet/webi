# Generated by Django 3.2.6 on 2021-09-28 19:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('blog_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('heading', models.CharField(max_length=200)),
                ('published_date', models.DateField(auto_now=True)),
                ('blog_content', ckeditor.fields.RichTextField(default='Blog content')),
            ],
        ),
    ]
