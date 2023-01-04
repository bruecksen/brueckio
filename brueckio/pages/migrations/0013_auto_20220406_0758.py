# Generated by Django 3.2.12 on 2022-04-06 07:58

from django.db import migrations, models
import pages.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_projectpage_is_highlight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['-title', 'name']},
        ),
        migrations.AddField(
            model_name='testimonial',
            name='is_highlight',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('contact_teaser', pages.blocks.ContactTeaserBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('cv', wagtail.blocks.StructBlock([('when', wagtail.blocks.CharBlock()), ('what', wagtail.blocks.RichTextBlock())])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))])), ('column_one_third', wagtail.blocks.StructBlock([('first', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))], label='Left')), ('second', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))], label='Right'))])), ('project_heading', wagtail.blocks.StructBlock([('lead_text', pages.blocks.RichTextBlock()), ('facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))])), ('testimonial', pages.blocks.TestimonialBlock(target_model='pages.Testimonial', template='blocks/testimonial_block.html'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectoverviewpage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('contact_teaser', pages.blocks.ContactTeaserBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('cv', wagtail.blocks.StructBlock([('when', wagtail.blocks.CharBlock()), ('what', wagtail.blocks.RichTextBlock())])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))])), ('column_one_third', wagtail.blocks.StructBlock([('first', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))], label='Left')), ('second', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))], label='Right'))])), ('project_heading', wagtail.blocks.StructBlock([('lead_text', pages.blocks.RichTextBlock()), ('facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))])), ('testimonial', pages.blocks.TestimonialBlock(target_model='pages.Testimonial', template='blocks/testimonial_block.html'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('contact_teaser', pages.blocks.ContactTeaserBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('cv', wagtail.blocks.StructBlock([('when', wagtail.blocks.CharBlock()), ('what', wagtail.blocks.RichTextBlock())])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))])), ('column_one_third', wagtail.blocks.StructBlock([('first', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))], label='Left')), ('second', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.blocks.CharBlock(label='Text', max_length=50))])), ('rich_text', pages.blocks.RichTextBlock()), ('lead_text', pages.blocks.LeadTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.blocks.CharBlock()), ('is_circle', wagtail.blocks.BooleanBlock(label='Show as a circle?', required=False))])), ('key_facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))], label='Right'))])), ('project_heading', wagtail.blocks.StructBlock([('lead_text', pages.blocks.RichTextBlock()), ('facts', wagtail.blocks.StructBlock([('facts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('fab fa-github-square', 'Github'), ('fa fa-link', 'Website'), ('fas fa-clock', 'Time'), ('fas fa-check-square', 'Jobs'), ('fa fa-microchip', 'Technologies'), ('django', 'Django'), ('wagtail', 'Wagtail'), ('bootstrap', 'Bootstrap')])), ('fact', wagtail.blocks.CharBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=False))], icon='fa-check')))]))])), ('testimonial', pages.blocks.TestimonialBlock(target_model='pages.Testimonial', template='blocks/testimonial_block.html'))], blank=True, null=True),
        ),
    ]
