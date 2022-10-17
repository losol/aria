from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models.functions import Coalesce

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel, PageChooserPanel)

from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable
from wagtail.models import Page

from core.blocks import FeaturedImageBlock, StoryBlock


class ArticlePage(Page):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    parent_page_types = ['core.WebSite']
    subpage_types = []

    template = "patterns/pages/standard_page.html"

    intro = models.TextField(blank=True)
    featured_image = StreamField(FeaturedImageBlock(), blank=True, use_json_field=True)
    story = StreamField(StoryBlock(), blank=True, use_json_field=True)
    license = models.ForeignKey(
        'utils.LicenseSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    publication_date = models.DateTimeField(
        null=True, blank=True,
        help_text="Use this field to override the date that the articles item appears to have been published."
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("featured_image"),
        FieldPanel("story"),
        InlinePanel('authors', label="Authors"),
        FieldPanel("license"),
        FieldPanel('publication_date'),
    ]

    @property
    def display_date(self):
        if self.publication_date:
            return self.publication_date
        else:
            return self.first_published_at


class ArticlePagePerson(Orderable):
    page = ParentalKey(
        ArticlePage,
        related_name='authors'
    )
    person = models.ForeignKey(
        'person.PersonPage',
        on_delete=models.CASCADE
    )
    biography = models.CharField(
        help_text="Override the author's biography in the article.",
        max_length=255,
        blank=True
    )

    panels = [
        PageChooserPanel('author'),
        FieldPanel('biography'),
    ]


class ArticleIndexPage(Page):
    class Meta:
        verbose_name = "Articles Index"

    template = 'patterns/pages/articles/articles_index.html'

    subpage_types = ['ArticlePage']
    parent_page_types = ['home.HomePage']

    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    def get_context(self, request, *args, **kwargs):
        articles = ArticlePage.objects.live().public().descendant_of(self).annotate(
            date=Coalesce('publication_date', 'first_published_at')
        ).order_by('-date')

        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(articles, settings.DEFAULT_PER_PAGE)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context = super().get_context(request, *args, **kwargs)
        context.update(
            articles=articles,
        )
        return context
