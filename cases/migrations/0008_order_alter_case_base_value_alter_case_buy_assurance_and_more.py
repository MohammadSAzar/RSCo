# Generated by Django 4.2.6 on 2023-11-13 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0007_remove_case_meter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('national_code', models.CharField(max_length=10, verbose_name='national_code')),
                ('address', models.CharField(max_length=1000, verbose_name='Address')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is_Paid?')),
                ('notes', models.CharField(max_length=1000, verbose_name='Notes')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='date & time of creation')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='date & time of modification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.AlterField(
            model_name='case',
            name='base_value',
            field=models.PositiveIntegerField(verbose_name='قیمت پایه'),
        ),
        migrations.AlterField(
            model_name='case',
            name='buy_assurance',
            field=models.BooleanField(default=False, verbose_name='ضمانت خرید'),
        ),
        migrations.AlterField(
            model_name='case',
            name='capacity',
            field=models.PositiveIntegerField(blank=True, verbose_name='ظرفیت'),
        ),
        migrations.AlterField(
            model_name='case',
            name='city',
            field=models.CharField(max_length=100, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='case',
            name='description',
            field=models.TextField(max_length=500, verbose_name='توضیحات پروژه'),
        ),
        migrations.AlterField(
            model_name='case',
            name='end_time',
            field=models.CharField(max_length=200, verbose_name='زمان اتمام'),
        ),
        migrations.AlterField(
            model_name='case',
            name='guaranteed_gain',
            field=models.BooleanField(default=False, verbose_name='سود تضمینی'),
        ),
        migrations.AlterField(
            model_name='case',
            name='guaranteed_gain_percent',
            field=models.PositiveIntegerField(verbose_name='درصد سود تضمینی'),
        ),
        migrations.AlterField(
            model_name='case',
            name='maker',
            field=models.CharField(max_length=100, verbose_name='سازنده'),
        ),
        migrations.AlterField(
            model_name='case',
            name='region',
            field=models.CharField(max_length=100, verbose_name='منطقه'),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('a', 'فعال'), ('s', 'به زودی ...'), ('e', 'خاتمه یافته')], max_length=10, verbose_name='وضعیت پروژه'),
        ),
        migrations.AlterField(
            model_name='case',
            name='title',
            field=models.CharField(max_length=300, verbose_name='پروژه'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter', models.PositiveIntegerField(default=1)),
                ('base_value', models.PositiveIntegerField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='cases.case')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='cases.order')),
            ],
        ),
    ]
