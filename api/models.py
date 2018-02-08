from django.db import models

from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')

    def __str__(self):
        return self.name


class Ep(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    ep_number = models.PositiveIntegerField(_('Ep number'))
    url_download = models.URLField(_('Link download'), unique=True)
    file_duration = models.CharField(_('Duration'), max_length=50)
    file_subtitles = models.CharField(_('Subtitles'), max_length=50)
    file_size = models.CharField(_('Size'), max_length=50)
    file_format = models.CharField(_('Format'), max_length=50)
    file_audio = models.CharField(_('Audio'), max_length=50)
    slug = models.SlugField(_('Slug'), unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Ep')
        verbose_name_plural = _('Eps')

    def __str__(self):
        return "{} - {}".format(self.title, self.ep_number)


class Anime(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    sinopse = models.TextField(_('Sinopse'), help_text='The item synopsis.')
    category = models.ManyToManyField(Category, verbose_name=_('Category'))
    ep = models.ManyToManyField(Ep, verbose_name=_('Eps'), blank=True)
    card_img = models.ImageField(
        _('Img file'), upload_to='danzou/anime', blank=True
    )
    card_img_url = models.URLField(_('Img url'), unique=True, blank=True)
    slug = models.SlugField(_('Slug'), unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Anime')
        verbose_name_plural = _('Animes')

    def __str__(self):
        return self.name
