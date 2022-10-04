from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class WebSite(Page):
    parent_page_types = ['wagtailcore.page']


@register_snippet
class LicenseSnippet(models.Model):
    title = models.TextField(blank=False)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, max_length=255)

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('url'),
    ]

    def __str__(self):
        return self.title
