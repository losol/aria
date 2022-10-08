from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from aria.core.blocks import StoryBlock


class PersonPage(Page):
    template = 'patterns/pages/person/person_page.html'

    parent_page_types = ['person.PersonIndexPage']

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    image = models.ForeignKey(
        'images.StandardImage',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    job_title = models.CharField(max_length=255, blank=True)

    intro = models.TextField(blank=True)
    story = StreamField(StoryBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('last_name'),
        ], heading="Name"),
        FieldPanel('image'),
        FieldPanel('job_title'),
        FieldPanel('intro'),
        FieldPanel('story')
    ]


class PersonIndexPage(Page):
    template = 'patterns/pages/people/person_index_page.html'

    parent_page_types = ['core.WebSite']
    subpage_types = ['PersonPage']

    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    class Meta:
        verbose_name = "People Index"

    def get_context(self, request, *args, **kwargs):
        people = PersonPage.objects.live().public().descendant_of(self).order_by('slug')

        context = super().get_context(request, *args, **kwargs)
        context.update(people=people)

        return context
