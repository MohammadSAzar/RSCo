# Generated by Django 4.2.6 on 2024-01-13 04:21

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_blog_cover_alter_blog_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده مقاله'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blogs.blogcategory', verbose_name='دسته مقاله'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن مقاله'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(upload_to='blogs/', verbose_name='تصویر مقاله'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_time_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_time_modification',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان بازبینی'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('pub', 'Published'), ('drf', 'Draft')], max_length=3, verbose_name='وضعیت مقاله'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان مقاله'),
        ),
    ]
