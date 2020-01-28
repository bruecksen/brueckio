
from wagtail.core.blocks import StructValue, StreamBlock, PageChooserBlock, StructBlock, CharBlock, \
    TextBlock, ListBlock, TimeBlock, DateBlock, ChoiceBlock, BooleanBlock, URLBlock, \
    IntegerBlock, RichTextBlock as _RichTextBlock, RawHTMLBlock as _RawHTMLBlock

from wagtail.images.blocks import ImageChooserBlock


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


class ContactTeaserBlock(TextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Contact Teaser'


class RichTextBlock(_RichTextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Rich Text'


class LeadTextBlock(_RichTextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Lead Text'
        template = 'blocks/lead_text_block.html'


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    description = CharBlock()


    class Meta:
        label = 'Image'
        template = 'blocks/image_block.html'


BASE_BLOCKS = [
    ('heading', HeadingBlock()),
    ('rich_text', RichTextBlock()),
    ('lead_text', LeadTextBlock()),
    ('contact_teaser', ContactTeaserBlock()),
    ('image', ImageBlock()),
    ('cv', CvBlock()),
]