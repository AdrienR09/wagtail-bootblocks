from wagtail.core import blocks

class PositionTypeBlock(blocks.StructBlock):
    type = blocks.ChoiceBlock(choices=[
        ("static", "static"),
        ("relative", "relative"),
        ("absolute", "absolute"),
        ("fixed", "fixed"),
        ("sticky", "sticky"),
        ("fixed-left", "fixed-left"),
        ("fixed-top", "fixed-top"),
        ("fixed-bottom", "fixed-bottom"),
        ("fixed-right", "fixed-right"),
        ("sticky-left", "sticky-left"),
        ("sticky-top", "sticky-top"),
        ("sticky-bottom", "sticky-bottom"),
        ("sticky-right", "sticky-right"),
    ], required=False, closed=True)

    class Meta:
        icon = "arrow-left"
        group = "position"
        template = "utilities/position/position_type_block.html"

class PositionArrangeBlock(blocks.StructBlock):
    position = blocks.ChoiceBlock(choices=[
        ("0", "0%"),
        ("50", "50%"),
        ("100", "100%"),
    ], required=False, closed=True)
    axis = blocks.ChoiceBlock(choices=[
        ("top", "top"),
        ("start", "start"),
        ("bottom", "bottom"),
        ("end", "end"),
    ], required=False, closed=True)

    class Meta:
        icon = "arrow-left"
        group = "position"
        template = "utilities/position/position_block.html"

class TranslationBlock(blocks.StructBlock):
    axis = blocks.ChoiceBlock(choices=[
        (None, "middle"),
        ("x", "x"),
        ("y", "y"),
    ], required=False, closed=True)

    class Meta:
        icon = "arrow-left"
        group = "position"
        template = "utilities/position/translation_block.html"

# Position streamblock :

class PositionBlock(blocks.StructBlock):

    type = PositionTypeBlock(required=False, closed=True)
    position = PositionArrangeBlock(required=False, closed=True)
    translate = TranslationBlock(required=False, closed=True)

    class Meta:
        icon = "arrow-left"
        group = "position"