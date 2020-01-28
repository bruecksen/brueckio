from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel

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
        context['projects'] = ProjectPage.objects.live()[:6]
        return context
 

class ContentPage(Page):
    parent_page_types = ['HomePage']

    content = StreamField(BASE_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]


class ProjectOverviewPage(Page):
    parent_page_types = ['HomePage']
    subpage_types = ['ProjectPage']

    content = StreamField(BASE_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    def get_context(self, value, parent_context=None):
        context = super(ProjectOverviewPage, self).get_context(value, parent_context=parent_context)
        context['projects'] = ProjectPage.objects.live()
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
    description = RichTextField()
    content = StreamField(BASE_BLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('description'),
        StreamFieldPanel('content'),
    ]