# Generated by Django 4.1.1 on 2022-10-08 18:42

import core.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(blank=True)),
                ('story', wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(icon='pilcrow', template='patterns/blocks/text_block.html')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.CharBlock(required=False)), ('alignment', core.blocks.ImageFormatChoiceBlock(default='full'))], label='Image', template='patterns/blocks/image_block.html')), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.CharBlock(required=False)), ('alignment', core.blocks.ImageFormatChoiceBlock(default='full'))])))], label='Image grid', template='patterns/blocks/image_grid_block.html')), ('pullquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('attribution', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], template='patterns/blocks/pullquote_block.html')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='code', label='Raw HTML', template='patterns/blocks/raw_html_block.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code', template='patterns/blocks/embed_block.html')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code', template='patterns/blocks/markdown_block.html'))], blank=True, use_json_field=True)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
