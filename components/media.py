from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .base import *

class ImageBlock(blocks.StructBlock):

    choices = [
        ("80x80", "80x80"),
        ("100x100", "100x100"),
        ("150x150", "150x150"),
        ("200x200", "200x200"),
        ("300x300", "300x300"),
        ("400x400", "400x400"),
        ("600x600", "600x600"),
        ("600x400", "600x400"),
        ("800x400", "800x400"),
        ("400x600", "400x600"),
        ("400x800", "400x800"),
        ("1200x600", "1200x600"),
        ("1510x600", "1510x600"),
        ("1800x800", "1800x800"),
        ("2000x800", "2000x800"),
    ]
    image = ImageChooserBlock(required=True, closed=True)
    dimensions = blocks.ChoiceBlock(choices=choices, closed=True, required=False)
    block = ImageBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/media/image_block.html"
        icon = "image"
        group = "media"

class CarouselBlock(blocks.StructBlock):

    cycle = blocks.IntegerBlock(min_value=0, max_value=60000, required=False, closed=True)
    display_controls = blocks.BooleanBlock(required=False, closed=True)
    display_indicators = blocks.BooleanBlock(required=False, closed=True)
    content = blocks.ListBlock(
        ImageBlock(closed=True),
        required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        icon = "order"
        template = "components/media/carousel_block.html"
        group = "media"