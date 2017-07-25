import arrow
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class Anime(models.Model):
    title = models.CharField(_('Name'), max_length=100)
    sinopse = models.TextField(_('Sinopse'))
    file_size = models.CharField(_('File Size'), max_length=50)
    duration = models.CharField(_('Duration'), max_length=50)
    file_format = models.CharField(
        _('File Format'), max_length=50, unique=True)
    file_audio = models.CharField(_('File Audio'), max_length=50, unique=True)
    file_subtitles = models.CharField(
        _('File Subtitles'), max_length=50, unique=True)
    url = models.URLField(_('Link Download'), unique=True)
    slug = models.SlugField(_('Slug'), max_length=140, unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Anime')
        verbose_name_plural = _('Animes')

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Anime.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    @property
    def time_ago(self):
        time_ago = arrow.get(self.created_at)
        return time_ago.humanize(locale='pt')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime:detail', kargs={'slug': self.slug})


class RelatedBugs(models.Model):
    name = models.CharField(_('Name'), max_length=30)
    email = models.EmailField(_('Email'), max_length=100)
    subject = models.CharField(_('Subject'), max_length=200)
    message = models.TextField(_('Message'), max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Related Bugs')
        verbose_name_plural = _('Relateds Bugs')

    def __str__(self):
        return self.subject
