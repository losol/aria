from django.db import models

from wagtail.images.models import AbstractImage, AbstractRendition, Image

# We define our own custom image class to replace wagtailimages.Image


class StandardImage(AbstractImage):

    description = models.TextField(
        blank=True,
        max_length=165,
    )
    author = models.CharField(
        blank=True,
        max_length=165,
        null=True,
    )
    image_source_url = models.URLField(
        blank=True
    )
    license = models.ForeignKey(
        'core.LicenseSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Insert custom fields below title
    custom_fields = (
        'description',
        'author',
        'image_source_url',
        'license'
    )

    admin_form_fields = Image.admin_form_fields + (
        'description',
        'author',
        'image_source_url',
        'license'
    )


class StandardRendition(AbstractRendition):
    image = models.ForeignKey(
        StandardImage,
        related_name='renditions',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
