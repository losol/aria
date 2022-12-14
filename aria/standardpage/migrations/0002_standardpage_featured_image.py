# Generated by Django 4.1.1 on 2022-10-08 18:54

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standardpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='featured_image',
            field=wagtail.fields.StreamField([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alt', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.CharBlock(required=False))], label='Image', template='patterns/blocks/image_block.html'))], blank=True, use_json_field=True),
        ),
    ]
