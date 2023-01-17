
import uuid
from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateBlock, IntegerBlock, ListBlock,
                                 PageChooserBlock)
from wagtail.blocks import RawHTMLBlock as _RawHTMLBlock
from wagtail.blocks import RichTextBlock as _RichTextBlock
from wagtail.blocks import (StreamBlock, StructBlock, StructValue,
                                 TextBlock, TimeBlock, URLBlock)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailfontawesome.blocks import IconBlock


class HeaderChoiceBlock(ChoiceBlock):
    choices = (
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6'),
    )


class HeadingBlock(StructBlock):
    heading = HeaderChoiceBlock(
        label='Header Size',
    )
    text = CharBlock(
        label='Text',
        max_length=50,
    )

    class Meta:
        label = 'Heading'
        template = 'blocks/heading_block.html'
        icon = 'fa-header'


class CvBlock(StructBlock):
    when = CharBlock()
    what = _RichTextBlock()

    class Meta:
        label = 'CV Entry'
        template = 'blocks/cv_block.html'
        icon = 'fa-clock'


class ContactTeaserBlock(_RichTextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Contact Teaser'
        template = 'blocks/contact_teaser_block.html'


class RichTextBlock(_RichTextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Rich Text'
        template = 'blocks/rich_text_block.html'


class TestimonialBlock(SnippetChooserBlock):
    pass

class LeadTextBlock(_RichTextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Lead Text'
        template = 'blocks/lead_text_block.html'


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    description = CharBlock(required=False)
    is_circle = BooleanBlock(label="Show as a circle?", required=False)
    is_full_width = BooleanBlock(required=False)
    content = StreamBlock([
        ('testimonial', TestimonialBlock(target_model='pages.Testimonial', template='blocks/testimonial_block.html')),
        ('rich_text', RichTextBlock()),
    ], required=False)


    class Meta:
        label = 'Image'
        template = 'blocks/image_block.html'
        icon = 'fa-image'

ICON_CHOICES = [
    ('fab fa-github-square', 'Github'),
    ('fa fa-link', 'Website'),
    ('fas fa-clock', 'Time'),
    ('fas fa-check-square', 'Jobs'),
    ('fa fa-microchip', 'Technologies'),
    ('django', 'Django'),
    ('wagtail', 'Wagtail'),
    ('bootstrap', 'Bootstrap'),
]


class KeyFactsBlock(StructBlock):
    facts = ListBlock(
        StructBlock(
            [
                ("icon", ChoiceBlock(required=True, choices=ICON_CHOICES)),
                ("fact", CharBlock(required=True)),
                ("link", URLBlock(required=False)),
            ], icon='fa-check'
        )
    )

    class Meta:
        label = 'Key facts'
        template = 'blocks/key_facts_block.html'
        icon = 'fa-check'


class ProjectHeading(StructBlock):
    lead_text = RichTextBlock()
    facts = KeyFactsBlock()

    class Meta:
        label = 'Project heading'
        template = 'blocks/project_heading_block.html'
        icon = 'fa-heading'


class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        return external_url or page.url


class LinkBlock(StructBlock):
    text = CharBlock(label="link text", required=True)
    page = PageChooserBlock(label="page", required=False)
    external_url = URLBlock(label="external URL", required=False)

    class Meta:
        value_class = LinkStructValue
        template = 'blocks/button_block.html'


COLUMN_BLOCKS = [
    ('heading', HeadingBlock()),
    ('rich_text', RichTextBlock()),
    ('lead_text', LeadTextBlock()),
    ('image', ImageBlock()),
    ('key_facts', KeyFactsBlock()),
    ('button', LinkBlock()),
    ('button_list', ListBlock(LinkBlock(), template='blocks/button_list_block.html')),
]


class ColumnOneThirdBlock(StructBlock):
    first = StreamBlock(COLUMN_BLOCKS, label="Left")
    second = StreamBlock(COLUMN_BLOCKS, label="Right")

    class Meta:
        icon = 'table'
        label = 'One Third (3,1)'
        template = 'blocks/columns-3-1_block.html'


class CollapseBlock(StructBlock):
    title = TextBlock()
    text = RichTextBlock()

    class Meta:
        label = 'Collapse'
        icon = 'fa-list'

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['id'] = uuid.uuid4()
        return context



BASE_BLOCKS = [
    ('heading', HeadingBlock()),
    ('rich_text', RichTextBlock()),
    ('html', _RawHTMLBlock()),
    ('lead_text', LeadTextBlock()),
    ('contact_teaser', ContactTeaserBlock()),
    ('image', ImageBlock()),
    ('collapse', ListBlock(CollapseBlock(), template='blocks/collapse_block.html')),
    ('cv', CvBlock()),
    ('key_facts', KeyFactsBlock()),
    ('column_one_third', ColumnOneThirdBlock()),
    ('project_heading', ProjectHeading()),
    ('testimonial', TestimonialBlock(target_model='pages.Testimonial', template='blocks/testimonial_block.html')),
    ('button', LinkBlock()),
    ('button_list', ListBlock(LinkBlock(), template='blocks/button_list_block.html')),
]