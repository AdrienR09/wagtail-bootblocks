from wagtail.core import blocks

from .text import *
from .position import *
from .display import *
from .components import *

class AddClassBlock(blocks.StructBlock):
    add_class = blocks.CharBlock(required=False)

    class Meta:
        icon = "code"
        template = "utilities/style/add_class_block.html"
        group = "special"

class StyleBlock(blocks.StreamBlock):

    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    container = ContainerBlock(required=False, closed=True)
    row = RowBlock(required=False, closed=True)
    column = ColumnBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)
    text_alignement = TextAlignementBlock(required=False, closed=True)

    display = DisplayBlock(required=False, closed=True)
    flex = FlexBlock(required=False, closed=True)
    float = FloatBlock(required=False, closed=True)

    type = PositionTypeBlock(required=False, closed=True)
    position = PositionArrangeBlock(required=False, closed=True)
    translate = TranslationBlock(required=False, closed=True)

    text = TextColorBlock(required=False, closed=True)
    background = BackgroundColorBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    shadow = ShadowBlock(required=False, closed=True)

    font = FontChooserBlock(required=False, closed=True)
    size = TextSizeChooserBlock(required=False, closed=True)
    weight = FontWeightChooserBlock(required=False, closed=True)
    decoration = TextDecorationChooserBlock(required=False, closed=True)
    overflow = TextOverflowChooserBlock(required=False, closed=True)
    special = SpecialTextBlock(required=False, closed=True)

class ButtonStyleBlock(blocks.StreamBlock):

    button_color = ButtonColorBlock(required=False, closed=True)
    button_size = ButtonSizeBlock(required=False, closed=True)
    button_disabled = DisableChooserBlock(required=False, closed=True)

    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    column = ColumnBlock(required=False, closed=True)
    text_alignement = TextAlignementBlock(required=False, closed=True)

    display = DisplayBlock(required=False, closed=True)
    flex = FlexBlock(required=False, closed=True)
    float = FloatBlock(required=False, closed=True)

    text = TextColorBlock(required=False, closed=True)
    background = BackgroundColorBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    shadow = ShadowBlock(required=False, closed=True)

    font = FontChooserBlock(required=False, closed=True)
    size = TextSizeChooserBlock(required=False, closed=True)
    weight = FontWeightChooserBlock(required=False, closed=True)
    decoration = TextDecorationChooserBlock(required=False, closed=True)
    overflow = TextOverflowChooserBlock(required=False, closed=True)
    special = SpecialTextBlock(required=False, closed=True)