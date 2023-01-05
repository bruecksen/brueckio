# Generated by Django 3.2.12 on 2023-01-05 13:24

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20230105_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='contact_banner_text',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='heropage',
            name='hero_text',
            field=wagtail.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='heropage',
            name='hero_title',
            field=wagtail.fields.RichTextField(),
        ),
    ]
