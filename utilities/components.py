from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .color import *

# Button blocks :

class ButtonColorBlock(blocks.StructBlock):
    color = ColorChooserBlock(required=False)
    outlined = blocks.BooleanBlock(required=False)

    class Meta:
        icon = "tick"
        template = "utilities/components/button_color_block.html"
        group = "button"

class ButtonSizeBlock(blocks.StructBlock):
    size = SizeChooserBlock(required=False)

    class Meta:
        icon = "view"
        template = "utilities/components/button_size_block.html"
        group = "button"

class DisableChooserBlock(blocks.StructBlock):
    choices = [
        ("disabled", "disabled"),
    ]

    class Meta:
        icon = "view"
        group = "button"

# Button block :

class ModalStyleBlock(blocks.StructBlock):
    choices = [
        ("fade", "fade"),
        ("scrollable", "modal-dialog-scrollable"),
        ("centered", "modal-dialog-centered"),
        ("small", "modal-sm"),
        ("large", "modal-lg"),
        ("extra-large", "modal-xl"),
        ("full-screen", "modal-fullscreen"),
        ("full-screen-sm", "full-screen-sm-down"),
        ("full-screen-md", "full-screen-md-down"),
        ("full-screen-lg", "full-screen-lg-down"),
        ("full-screen-xl", "full-screen-xl-down"),
        ("full-screen-xxl", "full-screen-xxl-down"),
    ]

    class Meta:
        icon = "pick"
        group = "container"
        template = "utilities/components/modal_style_block.html"


class PaginationSizeBlock(blocks.StructBlock):
    size = SizeChooserBlock(required=False)

    class Meta:
        icon = "view"
        group = "special"
        template = "utilities/components/button_size_block.html"

class BackgroundBlock(blocks.StructBlock):

    background = ImageChooserBlock(required=False, closed=True)

    class Meta:
        icon = "view"
        template = "utilities/components/background_block.html"