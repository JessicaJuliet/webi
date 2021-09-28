# Generated by Django 3.2.6 on 2021-09-28 19:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casestudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('website_url', models.URLField(max_length=1024)),
                ('github_url', models.URLField(max_length=1024)),
                ('heading', models.CharField(default='Heading', max_length=200)),
                ('case_study_content', ckeditor.fields.RichTextField(default='Case study content')),
            ],
            options={
                'verbose_name_plural': 'Casestudies',
            },
        ),
    ]
