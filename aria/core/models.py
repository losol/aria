from django.db import models
from modelcluster.models import ClusterableModel

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet


from wagtail.fields import StreamField


from aria.core.blocks import MenuBlock, StoryBlock


class WebSite(Page):
    template = 'patterns/pages/web_site.html'
    parent_page_types = ['wagtailcore.page']

    story = StreamField(StoryBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("story")
    ]


@register_setting(icon='list-ul')
class NavigationSettings(BaseSiteSetting, ClusterableModel):
    primary_navigation = StreamField(
        MenuBlock(),
        blank=True,
        help_text="Primary navigation"
    )
    footer_navigation = StreamField(
        MenuBlock(),
        blank=True,
        help_text="Links at the bottom."
    )
    footer_text = RichTextField(
        features=['bold', 'italic', 'link'],
        blank=True,
        help_text="Small print text at the bottom of all pages. Not required."
    )

    panels = [
        FieldPanel('primary_navigation'),
        FieldPanel('footer_navigation'),
        FieldPanel('footer_text'),
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
