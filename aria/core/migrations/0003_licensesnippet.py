# Generated by Django 4.1.1 on 2022-10-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_create_web_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True, max_length=255)),
            ],
        ),
    ]
