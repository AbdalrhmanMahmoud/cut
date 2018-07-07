from django.conf import settings
from django.db import models
from django_hosts.resolvers import reverse  # import the redirect method  third party
from .utils import create_shortcode   # generate random code
from .validators import validate_url, validate_dot_com  # import from validators.py
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class CutURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(CutURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs


class CutURL(models.Model):
    url = models.CharField(max_length=220,  validators=[validate_url, validate_dot_com] )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = CutURLManager()

    def save(self, *args, **kwargs):   # save links in database
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(CutURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):  # redirect def
        url_path = reverse("myc", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path
