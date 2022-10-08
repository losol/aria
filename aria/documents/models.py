from django.db import models

from wagtail.documents.models import AbstractDocument
from wagtail.documents.models import Document as WagtailDocument


class StandardDocument(AbstractDocument):
    description = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )
    source = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )
    license = models.ForeignKey(
        'core.LicenseSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    admin_form_fields = WagtailDocument.admin_form_fields + (
        'description',
        'license'
    )
