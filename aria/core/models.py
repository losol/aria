from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


from wagtail.fields import StreamField


from aria.core.blocks import MenuBlock, StoryBlock


class WebSite(Page):
    template = 'patterns/pages/web_site.html'
    parent_page_types = ['wagtailcore.page']

    story = StreamField(StoryBlock(), blank=True, use_json_field=True)

    header_menu = StreamField(MenuBlock(), blank=True, use_json_field=True)
    footer_menu = StreamField(MenuBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("story"),
        FieldPanel("header_menu"),
        FieldPanel("footer_menu")
    ]


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
