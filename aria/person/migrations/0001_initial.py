# Generated by Django 4.1.1 on 2022-10-10 16:29

import aria.core.blocks
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
        ('images', '0001_initial'),
        ('wagtailcore', '0077_alter_revision_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'People Index',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('intro', models.TextField(blank=True)),
                ('story', wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(icon='pilcrow', template='patterns/blocks/text_block.html')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.CharBlock(required=False)), ('alignment', aria.core.blocks.ImageFormatChoiceBlock(default='full'))], label='Image', template='patterns/blocks/image_block.html')), ('image_grid', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.CharBlock(required=False)), ('alignment', aria.core.blocks.ImageFormatChoiceBlock(default='full'))])))], label='Image grid', template='patterns/blocks/image_grid_block.html')), ('blockquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.RichTextBlock(form_classname='quote text')), ('attribution', wagtail.blocks.CharBlock(required=False)), ('attribution_url', wagtail.blocks.URLBlock(required=False))], template='patterns/blocks/blockquote_block.html')), ('pullquote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(form_classname='quote title')), ('attribution', wagtail.blocks.CharBlock(required=False))], template='patterns/blocks/pullquote_block.html')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='code', label='Raw HTML', template='patterns/blocks/raw_html_block.html')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code', template='patterns/blocks/embed_block.html')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code', template='patterns/blocks/markdown_block.html'))], blank=True, use_json_field=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.standardimage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
