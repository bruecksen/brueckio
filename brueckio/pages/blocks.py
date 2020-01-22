
from wagtail.core.blocks import StructValue, StreamBlock, PageChooserBlock, StructBlock, CharBlock, \
    TextBlock, ListBlock, TimeBlock, DateBlock, ChoiceBlock, BooleanBlock, URLBlock, \
    IntegerBlock, RichTextBlock as _RichTextBlock, RawHTMLBlock as _RawHTMLBlock

from wagtail.images.blocks import ImageChooserBlock


class HeadingBlock(CharBlock):

    class Meta:
        label = 'Heading'
        template = 'blocks/heading_block.html'
        icon = 'fa-header'


class ContactTeaserBlock(TextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Contact Teaser'


class RichTextBlock(_RichTextBlock):

    class Meta:
        icon = 'fa-file-text-o'
        label = 'Rich Text'


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    description = CharBlock()


    class Meta:
        label = 'Image'
        template = 'blocks/image_block.html'


BASE_BLOCKS = [
    ('heading', HeadingBlock()),
    ('rich_text', RichTextBlock()),
    ('contact_teaser', ContactTeaserBlock()),
    ('image', ImageBlock()),
]