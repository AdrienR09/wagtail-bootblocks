from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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
    ]

    class Meta:
        icon = "snippet"

class TextStyleChooserBlock(blocks.ChoiceBlock):

    ALERT = "alert"
    ALERT_DIS = "alert alert-dismissible fade show"
    BADGE = "badge"

    choices = [
        (ALERT, "alert"),
        (ALERT_DIS, "alert_dismissible"),
        (BADGE, "badge"),
    ]

    class Meta:
        icon = "arrows-up-down"

class TextAlignementChooserBlock(blocks.ChoiceBlock):

    LEFT = "text-left"
    RIGHT = "text-right"
    CENTER = "text-center"
    JUSTIFY = "text-justify"
    BREAK = "text-break"
    TRUNCATE = "text-truncate"
    WRAP = "text-wrap"
    NOWRAP = "text-nowrap"

    choices = [
        (LEFT, "left"),
        (RIGHT, "right"),
        (CENTER, "center"),
        (JUSTIFY, "justify"),
        (BREAK, "break"),
        (TRUNCATE, "truncate"),
        (WRAP, "wrap"),
        (NOWRAP, "nowrap"),
    ]

    class Meta:
        icon = "arrows-up-down"

class HorizontalAlignementChooserBlock(blocks.ChoiceBlock):

    START = "justify-content-start"
    CENTER = "justify-content-center"
    END = "justify-content-end"
    AROUND = "justify-content-around"
    BETWEEN = "justify-content-between"

    choices = [
        (START, "start"),
        (CENTER, "center"),
        (END, "end"),
        (AROUND, "around"),
        (BETWEEN, "between"),
    ]

    class Meta:
        icon = "arrows-up-down"

class VerticalAlignementChooserBlock(blocks.ChoiceBlock):

    START = "align-items-start"
    CENTER = "align-items-center"
    END = "align-items-end"

    choices = [
        (START, "start"),
        (CENTER, "center"),
        (END, "end"),
    ]

    class Meta:
        icon = "arrows-up-down"

class GridChooserBlock(blocks.ChoiceBlock):

    COL12 = "col-lg-12"
    COL11 = "col-lg-11"
    COL10 = "col-lg-10"
    COL9 = "col-lg-9"
    COL8 = "col-lg-8"
    COL7 = "col-lg-7"
    COL6 = "col-lg-6"
    COL5 = "col-lg-5"
    COL4 = "col-lg-4"
    COL3 = "col-lg-3"
    COL2 = "col-lg-2"
    COL1 = "col-lg-1"

    choices = [
        (COL12, "col-12"),
        (COL11, "col-11"),
        (COL10, "col-10"),
        (COL9, "col-9"),
        (COL8, "col-8"),
        (COL7, "col-7"),
        (COL6, "col-6"),
        (COL5, "col-5"),
        (COL4, "col-4"),
        (COL3, "col-3"),
        (COL2, "col-2"),
        (COL1, "col-1"),
    ]

    class Meta:
        icon = "grip"

class ShadowChooserBlock(blocks.ChoiceBlock):

    NONE = "shadow-none"
    SMALL = "shadow-sm"
    REGULAR = "shadow"
    LARGE = "shadow-lg"

    choices = [
        (NONE, "no shadow"),
        (SMALL, "small shadow"),
        (REGULAR, "regular shadow"),
        (LARGE, "large shadow"),
    ]

    class Meta:
        icon = "view"

class ContainerChooserBlock(blocks.ChoiceBlock):

    ROW = "row"
    NONE = "d-none"
    INLINE = "d-inline"
    INLINE_BLOCK = "d-inline-block"
    BLOCK = "d-block"
    TABLE = "d-table"
    TABLE_CELL = "d-table-cell"
    TABLE_ROW = "d-table-row"
    FLEX = "d-flex"
    INLINE_FLEX = "d-inline-flex"
    FLOAT_LEFT = "float-left"
    FLOAT_RIGHT = "float-right"

    choices = [
        (NONE , "none"),
        (ROW , "row"),
        (INLINE , "inline"),
        (INLINE_BLOCK , "inline-block"),
        (BLOCK , "block"),
        (TABLE , "table"),
        (TABLE_CELL , "table-cell"),
        (TABLE_ROW , "table-row"),
        (FLEX , "flex"),
        (INLINE_FLEX , "inline-flex"),
        (FLOAT_LEFT , "float-left"),
        (FLOAT_RIGHT , "float-right"),
    ]

    class Meta:
        icon = "placeholder"


class FixedPositionChooserBlock(blocks.ChoiceBlock):

    LEFT = "fixed-left"
    TOP = "fixed-top"
    BOTTOM = "fixed-bottom"
    RIGHT = "fixed-right"

    choices = [
        (LEFT, "left"),
        (TOP, "top"),
        (BOTTOM, "bottom"),
        (RIGHT, "right"),
    ]

    class Meta:
        icon = "arrows-up-down"

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

    class Meta:
        icon = "arrows-up-down"

class SizeWidthChooserBlock(blocks.ChoiceBlock):

    AUTO = "auto"
    W25 = "w-25"
    W50 = "w-50"
    W75 = "w-75"
    W100 = "w-100"

    choices = [
        (AUTO , "auto"),
        (W25 , "25%"),
        (W50 , "50%"),
        (W75 , "75%"),
        (W100 , "100%"),
    ]

    class Meta:
        icon = "arrows-up-down"

class SizeHeightChooserBlock(blocks.ChoiceBlock):

    AUTO = "auto"
    H25 = "h-25"
    H50 = "h-50"
    H75 = "h-75"
    H100 = "h-100"

    choices = [
        (AUTO , "auto"),
        (H25 , "25%"),
        (H50 , "50%"),
        (H75 , "75%"),
        (H100 , "100%"),
    ]

    class Meta:
        icon = "arrows-up-down"

class DimensionBlock(blocks.StreamBlock):

    height = SizeHeightChooserBlock(required=False)
    width = SizeWidthChooserBlock(required=False)

    class Meta:
        icon = "arrows-up-down"
        template = "style/dimension_block.html"

class ExtraDimensionBlock(blocks.StructBlock):

    max_height = blocks.IntegerBlock(min_value=1, max_value=50, required=False)
    min_height = blocks.IntegerBlock(min_value=1, max_value=50, required=False)
    height = blocks.IntegerBlock(min_value=1, max_value=50, required=False)
    max_width = blocks.IntegerBlock(min_value=1, max_value=50, required=False)
    min_width = blocks.IntegerBlock(min_value=1, max_value=50, required=False)
    width = blocks.IntegerBlock(min_value=1, max_value=50, required=False)

    class Meta:
        icon = "arrows-up-down"
        template = "style/extra_dimension_block.html"

class MarginBlock(blocks.StructBlock):

    size = blocks.IntegerBlock(min_value=-5, max_value=5)
    position = PositionChooserBlock(required=False)

    class Meta:
        icon = "placeholder"
        template = "style/margin_block.html"

class PaddingBlock(blocks.StructBlock):

    size = blocks.IntegerBlock(min_value=0, max_value=5)
    position = PositionChooserBlock(required=False)

    class Meta:
        icon = "placeholder"
        template = "style/padding_block.html"

# Borders :

class DisplayBorderChooserBlock(blocks.ChoiceBlock):

    BORDER = "border"
    TOP = "border-top"
    BOTTOM = "border-bottom"
    LEFT = "border-left"
    RIGHT = "border-right"
    NOBORDER = "border-0"
    NOTOP = "border-top-0"
    NOBOTTOM = "border-bottom-0"
    NOLEFT = "border-left-0"
    NORIGHT = "border-right-0"

    choices = [
        (BORDER, "border"),
        (TOP, "border-top"),
        (BOTTOM, "border-bottom"),
        (LEFT, "border-left"),
        (RIGHT, "border-right"),
        (NOBORDER, "no border"),
        (NOTOP, "no border-top"),
        (NOBOTTOM, "no border-bottom"),
        (NOLEFT, "no border-left"),
        (NORIGHT, "no border-right"),
    ]

    class Meta:
        icon = "arrows-up-down"

class BorderRadiusChooserBlock(blocks.ChoiceBlock):

    NONE = "rounded-0"
    ROUNDED = "rounded"
    TOP = "rounded-top"
    BOTTOM = "rounded-bottom"
    LEFT = "rounded-left"
    RIGHT = "rounded-right"
    CIRCLE = "rounded-circle"
    PILL = "rounded-pill"

    choices = [
        (NONE, "rounded-0"),
        (ROUNDED, "rounded"),
        (TOP, "rounded-top"),
        (BOTTOM, "rounded-bottom"),
        (LEFT, "rounded-left"),
        (RIGHT, "rounded-right"),
        (CIRCLE, "rounded-circle"),
        (PILL, "rounded-pill"),
    ]


class BorderBlock(blocks.StructBlock):

    border_style = DisplayBorderChooserBlock(required=False)
    border_radius = BorderRadiusChooserBlock(required=False)
    border_color = ColorChooserBlock(required=False)

    class Meta:
        icon = "radio-empty"
        template = "style/border_block.html"

