import uuid

from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from .blocks import BASE_BLOCKS


class HomePage(Page):
    parent_page_types = ['wagtailcore.page']
    max_count_per_parent = 1

    introduction = RichTextField(blank=True, default="")

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    def get_context(self, value, parent_context=None):
        context = super(HomePage, self).get_context(value, parent_context=parent_context)
        context['projects'] = ProjectPage.objects.live().filter(is_highlight=True).order_by('?')[:3]
        context['uuid'] = uuid.uuid4()
        return context
 

class ContentPage(Page):
    parent_page_types = ['HomePage']

    content = StreamField(BASE_BLOCKS, null=True, blank=True, use_json_field=True)
    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]


class HeroPage(Page):
    parent_page_types = ['HomePage']
    hero_title = RichTextField()
    hero_text = RichTextField()
    content = StreamField(BASE_BLOCKS, null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_title'),
                FieldPanel('hero_text'),
            ]
        ),
        FieldPanel('content'),
    ]


class ContactPage(ContentPage):
    pass


class ProjectOverviewPage(Page):
    parent_page_types = ['HomePage']
    subpage_types = ['ProjectPage']

    content = StreamField(BASE_BLOCKS, null=True, blank=True, use_json_field=True)
    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['projects'] = ProjectPage.objects.live().order_by('-first_published_at')
        return context



class ProjectPage(Page):
    parent_page_types = ['ProjectOverviewPage']

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, 
        blank=True,
        on_delete=models.PROTECT,
        related_name='+'
    )
    is_highlight = models.BooleanField(default=False)
    description = RichTextField()
    content = StreamField(BASE_BLOCKS, null=True, blank=True, use_json_field=True)
    contact_banner_text = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('is_highlight'),
        FieldPanel('image'),
        FieldPanel('description'),
        FieldPanel('contact_banner_text'),
        FieldPanel('content'),
    ]

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        if self.contact_banner_text:
            context['contact_banner_text'] = self.contact_banner_text
        return context

@register_snippet
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(
        'pages.ProjectPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='testimonials'
    )
    text = models.TextField()
    is_highlight = models.BooleanField(default=False)

    panels = [
        FieldPanel('name'),
        FieldPanel('is_highlight'),
        FieldPanel('title'),
        FieldPanel('project'),
        FieldPanel('text'),
    ]

    class Meta:
        # abstract = True
        ordering = ['-title', 'name']

    def __str__(self):
        return self.name
