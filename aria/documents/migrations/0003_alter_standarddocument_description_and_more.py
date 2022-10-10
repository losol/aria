# Generated by Django 4.1.1 on 2022-10-10 14:32

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_standarddocument_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standarddocument',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, help_text='Small print text at the bottom of all pages. Not required.'),
        ),
        migrations.AlterField(
            model_name='standarddocument',
            name='source',
            field=wagtail.fields.RichTextField(blank=True, help_text='Small print text at the bottom of all pages. Not required.'),
        ),
    ]
