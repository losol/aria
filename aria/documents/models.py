from django.db import models

from wagtail.documents.models import AbstractDocument
from wagtail.documents.models import Document as WagtailDocument


class StandardDocument(AbstractDocument):

    description = models.CharField(blank=True, max_length=512)
    source = models.CharField(blank=True, max_length=255)
    source_url = models.URLField(blank=True)

    license = models.ForeignKey(
        'core.LicenseSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    admin_form_fields = WagtailDocument.admin_form_fields + (
        'description',
        'source',
        'source_url',
        'license'
    )
