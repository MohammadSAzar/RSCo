from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(BlogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    STATUS_CHOICES = (('pub', 'Published'), ('drf', 'Draft'))
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name='posts')
    title = models.CharField(max_length=200, verbose_name=_('Blog Title'))
    body = RichTextField(verbose_name=_('Text'))
    date_time_creation = models.DateTimeField(auto_now_add=True)
    date_time_modification = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True, allow_unicode=True)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date_time_modification',)

    def __str__(self):
        return self.title + '|' + str(self.author)

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[self.slug])

