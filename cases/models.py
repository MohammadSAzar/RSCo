from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _
from django.conf import settings
from ckeditor.fields import RichTextField


class Case(models.Model):
    STATUS = [
        ('a', _('Active')),
        ('s', _('Soon')),
        ('e', _('Ended')),
    ]
    title = models.CharField(max_length=300, verbose_name=_('Title'))
    maker = models.CharField(max_length=100, verbose_name=_('Maker'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    region = models.CharField(max_length=100, verbose_name=_('Region'))
    capacity = models.PositiveIntegerField(blank=True, verbose_name=_('Capacity'))
    base_value = models.PositiveIntegerField(verbose_name=_('Min of investment'))
    buy_assurance = models.BooleanField(default=False, verbose_name=_('Buy assurance'))
    guaranteed_gain = models.BooleanField(default=False, verbose_name=_('Guaranteed gain'))
    guaranteed_gain_percent = models.PositiveIntegerField(verbose_name=_('Guaranteed gain percent'))
    end_time = models.CharField(max_length=200, verbose_name=_('End time'))
    description = RichTextField(verbose_name=_('Description'))
    status = models.CharField(max_length=10, choices=STATUS, verbose_name=_('Status'))
    cover = models.ImageField(upload_to='cases/', blank=True, verbose_name=_('Cover'))
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True, allow_unicode=True)
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date and time of creation'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Case, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-datetime_created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case_detail', args=[self.slug])


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    first_name = models.CharField(max_length=150, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Last Name'))
    phone = models.CharField(max_length=11, verbose_name=_('Phone Number'))
    national_code = models.CharField(max_length=10, verbose_name=_('National Code'))
    address = models.CharField(max_length=1000, verbose_name=_('Address'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Payment Status'))
    notes = models.CharField(max_length=1000, verbose_name=_('Notes'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date & time of creation'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date & time of modification'))

    def get_total_price(self):
        return sum(item.meter*item.price for item in self.item.all())

    def __str__(self):
        return f'Order: {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item', verbose_name=_('Order'))
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='order_items', verbose_name=_('Project'))
    meter = models.PositiveIntegerField(default=1, verbose_name=_('Area'))
    base_value = models.PositiveIntegerField(verbose_name=_('Base value'))

    def __str__(self):
        return f'Order Item {self.id}: {self.case}x{self.meter}'



