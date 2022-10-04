"""
  @Credit: Based on the work of Torchbox
  @Links: https://github.com/torchbox/wagtail-torchbox/blob/master/tbx/core/blocks.py
"""

from django import forms
from wagtailmarkdown.blocks import MarkdownBlock

from wagtail.blocks import (
    CharBlock,
    FieldBlock,
    ListBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(
        choices=(
            ("left", "Wrap left"),
            ("right", "Wrap right"),
            ("full", "Full width"),
            ("wide", "Wide image"),
        )
    )


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    alt = CharBlock(required=False)
    caption = CharBlock(required=False)
    alignment = ImageFormatChoiceBlock(default="full")

    class Meta:
        icon = "image"


class ImageGridBlock(StructBlock):
    images = ListBlock(ImageBlock())

    class Meta:
        icon = "grip"


class PullQuoteBlock(StructBlock):
    quote = CharBlock(form_classname="quote title")
    attribution = CharBlock()
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = "openquote"


class StoryBlock(StreamBlock):
    text = RichTextBlock(
        icon="pilcrow",
        template="patterns/blocks/text_block.html",
    )
    image = ImageBlock(
        label="Image",
        template="patterns/blocks/image_block.html",
    )
    image_grid = ImageGridBlock(
        label="Image grid",
        template="patterns/blocks/image_grid_block.html",
    )
    pullquote = PullQuoteBlock(
        template="patterns/blocks/pullquote_block.html"
    )
    raw_html = RawHTMLBlock(
        label="Raw HTML",
        icon="code",
        template="patterns/blocks/raw_html_block.html",
    )
    embed = EmbedBlock(
        icon="code",
        template="patterns/blocks/embed_block.html",
    )
    markdown = MarkdownBlock(
        icon="code",
        template="patterns/blocks/markdown_block.html",
    )

    class Meta:
        template = "patterns/blocks/default_block.html"
