from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


from .layout import *

# Base blocks :

class ColorChooserBlock(blocks.ChoiceBlock):
    MUTED = "muted"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    WARNING = "warning"
    DANGER = "danger"
    SUCCESS = "success"
    INFO = "info"
    WHITE = "white"
    DARK = "dark"
    LIGHT = "light"
    TRANS = "transparent"
    COLOR1 = "color1"
    COLOR2 = "color2"
    COLOR3 = "color3"
    COLOR4 = "color4"
    COLOR5 = "color5"
    COLOR6 = "color6"
    COLOR7 = "color7"

    choices = [
        (MUTED, "muted"),
        (PRIMARY, "primary"),
        (SECONDARY, "secondary"),
        (WARNING, "warning"),
        (DANGER, "danger"),
        (SUCCESS, "success"),
        (INFO, "info"),
        (WHITE, "white"),
        (DARK, "dark"),
        (LIGHT, "light"),
        (TRANS, "transparent"),
        (COLOR1, "color1"),
        (COLOR2, "color2"),
        (COLOR3, "color3"),
        (COLOR4, "color4"),
        (COLOR5, "color5"),
        (COLOR6, "color6"),
        (COLOR7, "color7"),
    ]

    class Meta:
        icon = "snippet"

# Color blocks :

class TextColorBlock(blocks.StructBlock):
    text_color = ColorChooserBlock()

    class Meta:
        icon = "snippet"
        template = "utilities/color/text_color_block.html"
        group = "color"

class BackgroundColorBlock(blocks.StructBlock):
    background_color = ColorChooserBlock(closed=True, required=False)
    gradient = blocks.BooleanBlock(closed=True, required=False)

    class Meta:
        icon = "snippet"
        template = "utilities/color/background_color_block.html"
        group = "color"

class BorderBlock(blocks.StructBlock):
    border_style = blocks.ChoiceBlock(choices=[
        ("border-0", "no border"),
        ("border", "border"),
        ("border-top", "border-top"),
        ("border-bottom", "border-bottom"),
        ("border-left", "border-left"),
        ("border-right", "border-right"),
        ("border-top-0", "no border-top"),
        ("border-bottom-0", "no border-bottom"),
        ("border-left-0", "no border-left"),
        ("border-right-0", "no border-right"),
    ], required=False, closed=True)
    border_shape = blocks.ChoiceBlock(choices=[
        ("rounded-0", "rounded-0"),
        ("rounded", "rounded"),
        ("rounded-top", "rounded-top"),
        ("rounded-bottom", "rounded-bottom"),
        ("rounded-left", "rounded-left"),
        ("rounded-right", "rounded-right"),
        ("rounded-circle", "rounded-circle"),
        ("rounded-pill", "rounded-pill"),
    ], required=False, closed=True)
    border_color = ColorChooserBlock(required=False)

    class Meta:
        icon = "placeholder"
        template = "utilities/color/border_block.html"
        group = "color"

class ShadowBlock(blocks.StructBlock):
    size = SizeChooserBlock(required=False, closed=True)
    gradient = blocks.BooleanBlock(required=False, closed=True)

    class Meta:
        icon = "view"
        template = "utilities/color/shadow_block.html"
        group = "color"


class BackgroundBlock(blocks.StreamBlock):

    image = ImageChooserBlock(required=False, closed=True)

    class Meta:
        icon = "view"
        template = "utilities/color/background_block.html"
        group = "color"

# Color streamblock :

class ColorBlock(blocks.StreamBlock):

    text = TextColorBlock(required=False, closed=True)
    background = BackgroundColorBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    shadow = ShadowBlock(required=False, closed=True)

    class Meta:
        group = "color"
        icon = "spinner"