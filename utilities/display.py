from wagtail.core import blocks

from .layout import *

class DisplayBlock(blocks.StructBlock):
    type = blocks.ChoiceBlock(choices=[
        ("none", "none"),
        ("inline", "inline"),
        ("inline-block", "inline-block"),
        ("block", "block"),
        ("table", "table"),
        ("cell", "table-cell"),
        ("row", "table-row"),
        ("flex", "flex"),
        ("inline-flex", "inline-flex"),
    ], required=True, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "spinner"
        group = "display"
        template = "style/display_block.html"

class FlexBlock(blocks.StructBlock):
    type = blocks.ChoiceBlock(choices=[
        ("row", "row"),
        ("row-reverse", "row-reverse"),
        ("column", "column"),
        ("column-reverse", "column-reverse"),
        ("fill", "fill"),
        ("wrap", "wrap"),
        ("wrap-reverse", "wrap-reverse"),
        ("nowrap", "nowrap"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "spinner"
        group = "display"
        template = "style/flex_block.html"

class FloatBlock(blocks.StructBlock):
    type = blocks.ChoiceBlock(choices=[
        ("start", "start"),
        ("none", "none"),
        ("end", "end"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "spinner"
        group = "display"
        template = "style/float_block.html"

# Display streamblock :

class DisplayBlock(blocks.StreamBlock):

    display = DisplayBlock(required=False, closed=True)
    flex = FlexBlock(required=False, closed=True)
    float = FloatBlock(required=False, closed=True)

    class Meta:
        group = "display"
        icon = "spinner"