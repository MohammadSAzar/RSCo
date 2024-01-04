# Generated by Django 4.2.6 on 2024-01-04 11:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Blog Title')),
                ('body', ckeditor.fields.RichTextField(verbose_name='متن')),
                ('date_time_creation', models.DateTimeField(auto_now_add=True)),
                ('date_time_modification', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pub', 'Published'), ('drf', 'Draft')], max_length=3)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blogs.blogcategory')),
            ],
            options={
                'ordering': ('-date_time_modification',),
            },
        ),
    ]
