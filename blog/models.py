from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    STATUS_CHOICES = (('pub', 'Published'), ('drf', 'Draft'))
    blog_title = models.CharField(max_length=200, verbose_name=_('Blog Title'))
    text = RichTextField(verbose_name=_('Text'))
    date_time_creation = models.DateTimeField(auto_now_add=True)
    date_time_modification = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title)
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date_time_modification',)

    def __str__(self):
        return self.blog_title

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[self.slug])


