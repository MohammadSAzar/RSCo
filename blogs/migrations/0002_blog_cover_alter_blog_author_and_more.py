# Generated by Django 4.2.6 on 2024-01-06 16:31

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(blank=True, default='img/blog/blog-02', upload_to='blogs/', verbose_name='Blog Cover'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Blog Author'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blogs.blogcategory', verbose_name='Blog Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Blog Body'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_time_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Datetime of Creation'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_time_modification',
            field=models.DateTimeField(auto_now=True, verbose_name='Datetime of Modification'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('pub', 'Published'), ('drf', 'Draft')], max_length=3, verbose_name='Blog Status'),
        ),
    ]
