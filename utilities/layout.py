from wagtail.core import blocks

# Base blocks :

class BreakpointChooserBlock(blocks.ChoiceBlock):
    choices = [("xs", "extra-small"),
               ("sm", "small"),
               ("md", "medium"),
               ("lg", "large"),
               ("xl", "extra-large")]

class PositionChooserBlock(blocks.ChoiceBlock):
    ALL = ""
    LEFT = "l"
    TOP = "t"
    BOTTOM = "b"
    RIGHT = "r"
    VERTICAL = "y"
    HORIZONTAL = "x"

    choices = [
        (ALL, "everywhere"),
        (LEFT, "left"),
        (TOP, "top"),
        (BOTTOM, "bottom"),
        (RIGHT, "right"),
        (VERTICAL, "vertical"),
        (HORIZONTAL, "horizontal"),
    ]

class SizeChooserBlock(blocks.ChoiceBlock):
    NONE = "none"
    SMALL = "sm"
    STANDARD = None
    LARGE = "lg"

    choices = [
        (NONE, "none"),
        (SMALL, "small"),
        (STANDARD, "standard"),
        (LARGE, "large"),
    ]


# Layout blocks :

class MarginBlock(blocks.StructBlock):
    size = blocks.ChoiceBlock(choices=[
        ("auto", "auto"),
        ("n5", "-5"),
        ("n4", "-4"),
        ("n3", "-3"),
        ("n2", "-2"),
        ("n1", "-1"),
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ], required=False, closed=True)
    position = PositionChooserBlock(required=False)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "radio-full"
        template = "utilities/layout/margin_block.html"
        group = "layout"

class PaddingBlock(blocks.StructBlock):
    size = blocks.ChoiceBlock(choices=[
        ("auto", "auto"),
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ], required=False, closed=True)
    position = PositionChooserBlock(required=False)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "radio-empty"
        template = "utilities/layout/padding_block.html"
        group = "layout"

class ContainerBlock(blocks.StructBlock):

    breakpoints = blocks.ChoiceBlock(choices=[
        ("fluid", "fluid"),
        ("xs", "extra-small"),
        ("sm", "small"),
        ("md", "medium"),
        ("lg", "large"),
        ("xl", "extra-large"),
    ], required=False, closed=True)


    class Meta:
        icon = "spinner"
        group = "layout"
        template = "utilities/layout/container_block.html"

class RowBlock(blocks.StructBlock):

    columns = blocks.IntegerBlock(min_value=0, max_value=12, required=False, closed=True)

    class Meta:
        icon = "spinner"
        group = "layout"
        template = "utilities/layout/row_block.html"

class ColumnBlock(blocks.StructBlock):
    columns = blocks.IntegerBlock(min_value=0, max_value=12, required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "grip"
        group = "layout"
        template = "utilities/layout/column_block.html"

class HorizontalAlignementBlock(blocks.StructBlock):
    alignement = blocks.ChoiceBlock(choices=[
        ("start", "start"),
        ("center", "center"),
        ("end", "end"),
        ("around", "around"),
        ("between", "between"),
    ], required=False, closed=True)
    breakpoint = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "arrow-right"
        group = "layout"
        template = "utilities/layout/horizontal_alignement_block.html"

class VerticalAlignementBlock(blocks.StructBlock):
    alignement = blocks.ChoiceBlock(choices=[
        ("start", "start"),
        ("center", "center"),
        ("end", "end"),
        ("stretch", "stretch"),
        ("baseline", "baseline"),
    ], required=False, closed=True)
    item = blocks.ChoiceBlock(choices=[
        ("items", "items"),
        ("self", "self"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "arrow-up"
        group = "layout"
        template = "utilities/layout/vertical_alignement_block.html"

# Layout streamblock :

class LayoutBlock(blocks.StreamBlock):

    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    container = ContainerBlock(required=False, closed=True)
    row = RowBlock(required=False, closed=True)
    column = ColumnBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)

    class Meta:
        group = "layout"
        icon = "arrow-up"