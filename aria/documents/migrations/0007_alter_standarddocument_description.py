# Generated by Django 4.1.1 on 2022-10-10 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_alter_standarddocument_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standarddocument',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
