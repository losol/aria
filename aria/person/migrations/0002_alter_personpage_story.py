# Generated by Django 4.1.1 on 2022-10-08 22:02

import aria.core.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='story',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(icon='pilcrow', template='patterns/blocks/text_block.html')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.CharBlock(required=False)), ('alignment', aria.core.blocks.ImageFormatChoiceBlock(default='full'))], label='Image', template='patterns/blocks/image_block.html')), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.CharBlock(required=False)), ('alignment', aria.core.blocks.ImageFormatChoiceBlock(default='full'))])))], label='Image grid', template='patterns/blocks/image_grid_block.html')), ('pullquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('attribution', wagtail.blocks.CharBlock(required=False))], template='patterns/blocks/pullquote_block.html')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='code', label='Raw HTML', template='patterns/blocks/raw_html_block.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code', template='patterns/blocks/embed_block.html')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code', template='patterns/blocks/markdown_block.html'))], blank=True, use_json_field=True),
        ),
    ]
