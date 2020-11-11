from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# Chooser blocks :

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

class SizeChooserBlock(blocks.ChoiceBlock):
    NONE = "-none"
    SMALL = "-sm"
    STANDARD = ""
    LARGE = "-lg"

    choices = [
        (NONE, "None"),
        (SMALL, "Small"),
        (STANDARD, "Standard"),
        (LARGE, "Large"),
    ]

class BreakpointChooserBlock(blocks.ChoiceBlock):

    choices = [("xs" ,"extra-small"),
    ("sm" ,"small"),
    ("md", "medium"),
    ("lg", "large"),
    ("xl", "extra-large")]

# Text blocks :

class FontChooserBlock(blocks.ChoiceBlock):

    DEFAULT = "default"
    FIRST = "first-font"
    SECOND = "second-font"
    THIRD = "third-font"

    choices = [
        (DEFAULT, "default"),
        (FIRST, "first-font"),
        (SECOND, "second-font"),
        (THIRD, "third-font"),
    ]

    class Meta:
        icon = "pilcrow"
        group = "text"

class TextSizeBlock(blocks.StructBlock):

    size = blocks.IntegerBlock(min_value=1, max_value=6)

    class Meta:
        icon = "arrows-up-down"
        template = "style/text_size_block.html"
        group = "text"

class TextColorBlock(blocks.StructBlock):

    text_color = ColorChooserBlock()

    class Meta:
        icon = "snippet"
        template = "style/text_color_block.html"
        group = "text"

class TextOverflowChooserBlock(blocks.ChoiceBlock):

    BREAK = "text-break"
    TRUNCATE = "text-truncate"
    WRAP = "text-wrap"
    NOWRAP = "text-nowrap"

    choices = [
        (BREAK, "break"),
        (TRUNCATE, "truncate"),
        (WRAP, "wrap"),
        (NOWRAP, "nowrap"),
    ]

    class Meta:
        icon = "redirect"
        group = "text"

class BadgeBlock(blocks.StructBlock):

    color = ColorChooserBlock(required=False, closed=True)
    pill = blocks.BooleanBlock(required=False, closed=True)

    class Meta:
        template = "style/badge_block.html"
        group = "text"
        label = "badge"

# Button blocks :

class ButtonColorBlock(blocks.StructBlock):

    color = ColorChooserBlock(required=False)
    outlined = blocks.BooleanBlock(required=False)

    class Meta:
        icon = "tick"
        template = "style/button_color_block.html"
        group = "button"

class ButtonSizeBlock(blocks.StructBlock):

    size = SizeChooserBlock(required=False)

    class Meta:
        icon = "view"
        template = "style/button_size_block.html"
        group = "button"

# Image blocks :

class ImageDimensionsChooser(blocks.ChoiceBlock):

    choices = [
        ("80x80","80x80"),
        ("100x100","100x100"),
        ("150x150","150x150"),
        ("200x200","200x200"),
        ("300x300","300x300"),
        ("400x400","400x400"),
        ("600x600","600x600"),
        ("600x400","600x400"),
        ("800x400","800x400"),
    ]

    class Meta:
        group = "image"

# Content blocks :

class BackgroundColorBlock(blocks.StructBlock):

    background_color = ColorChooserBlock(required=False)

    class Meta:
        icon = "snippet"
        template = "style/background_color_block.html"
        group = "content"

class TextAlignementBlock(blocks.StructBlock):

    alignement = blocks.ChoiceBlock(choices = [
        ("left", "left"),
        ("right", "right"),
        ("center", "center"),
        ("justify", "justify"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "horizontalrule"
        group = "content"
        template = "style/text_alignement_block.html"

class HorizontalAlignementBlock(blocks.StructBlock):

    alignement = blocks.ChoiceBlock(choices = [
        ("start", "start"),
        ("center", "center"),
        ("end", "end"),
        ("around", "around"),
        ("between", "between"),
    ], required=False, closed=True)
    breakpoint = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "arrow-right"
        group = "content"
        template = "style/horizontal_alignement_block.html"

class VerticalAlignementBlock(blocks.StructBlock):

    alignement = blocks.ChoiceBlock(choices = [
        ("start", "start"),
        ("center", "center"),
        ("end", "end"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "arrow-up"
        group = "content"
        template = "style/vertical_alignement_block.html"

# Box blocks :

class MarginBlock(blocks.StructBlock):

    size = blocks.IntegerBlock(min_value=-5, max_value=5)
    position = PositionChooserBlock(required=False)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "radio-full"
        template = "style/margin_block.html"
        group = "box"

class PaddingBlock(blocks.StructBlock):

    size = blocks.IntegerBlock(min_value=0, max_value=5)
    position = PositionChooserBlock(required=False)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "radio-empty"
        template = "style/padding_block.html"
        group = "box"

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
        icon = "arrow-down"
        group = "box"

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
        icon = "arrow-up"
        group = "box"

class ColumnsBlock(blocks.StructBlock):

    columns = blocks.IntegerBlock(min_value=0, max_value=12, required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "grip"
        group = "box"
        template = "style/column_block.html"

class DisplayChooserBlock(blocks.ChoiceBlock):

    NONE = "d-none"
    INLINE = "d-inline"
    INLINE_BLOCK = "d-inline-block"
    BLOCK = "d-block"
    TABLE = "d-table"
    TABLE_CELL = "d-table-cell"
    TABLE_ROW = "d-table-row"
    FLEX = "d-flex"
    FLEX_COLUMN = "flex-column"
    INLINE_FLEX = "d-inline-flex"
    FLOAT_LEFT = "float-left"
    FLOAT_RIGHT = "float-right"

    choices = [
        (NONE , "none"),
        (INLINE , "inline"),
        (INLINE_BLOCK , "inline-block"),
        (BLOCK , "block"),
        (TABLE , "table"),
        (TABLE_CELL , "table-cell"),
        (TABLE_ROW , "table-row"),
        (FLEX , "flex"),
        (FLEX_COLUMN , "flex-column"),
        (INLINE_FLEX , "inline-flex"),
        (FLOAT_LEFT , "float-left"),
        (FLOAT_RIGHT , "float-right"),
    ]

    class Meta:
        icon = "spinner"
        group = "box"

class ShadowSizeBlock(blocks.StructBlock):

    size = SizeChooserBlock(required=False)

    class Meta:
        icon = "view"
        template = "style/shadow_size_block.html"
        group = "box"

class DimensionBlock(blocks.StructBlock):

    height = blocks.IntegerBlock(min_value=1, max_value=500, required=False)
    width = blocks.IntegerBlock(min_value=1, max_value=500, required=False)

    class Meta:
        icon = "arrows-up-down"
        template = "style/dimension_block.html"
        group = "box"

class BorderBlock(blocks.StructBlock):

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

    NONE = "rounded-0"
    ROUNDED = "rounded"
    TOP = "rounded-top"
    BOTTOM = "rounded-bottom"
    LEFT = "rounded-left"
    RIGHT = "rounded-right"
    CIRCLE = "rounded-circle"
    PILL = "rounded-pill"

    border_style = blocks.ChoiceBlock(choices = [
        (NOBORDER, "no border"),
        (BORDER, "border"),
        (TOP, "border-top"),
        (BOTTOM, "border-bottom"),
        (LEFT, "border-left"),
        (RIGHT, "border-right"),
        (NOTOP, "no border-top"),
        (NOBOTTOM, "no border-bottom"),
        (NOLEFT, "no border-left"),
        (NORIGHT, "no border-right"),
    ], required=False)
    border_shape = blocks.ChoiceBlock(choices = [
        (NONE, "rounded-0"),
        (ROUNDED, "rounded"),
        (TOP, "rounded-top"),
        (BOTTOM, "rounded-bottom"),
        (LEFT, "rounded-left"),
        (RIGHT, "rounded-right"),
        (CIRCLE, "rounded-circle"),
        (PILL, "rounded-pill"),
    ], required=False)
    border_color = ColorChooserBlock(required=False)

    class Meta:
        icon = "placeholder"
        template = "style/border_block.html"
        group = "box"

# Other :

class SpecialTextChooserBlock(blocks.ChoiceBlock):

    ALERT = "alert"
    ALERT_DIS = "alert alert-dismissible fade show"
    BADGE = "badge"

    choices = [
        (ALERT, "alert"),
        (ALERT_DIS, "alert_dismissible"),
        (BADGE, "badge"),
    ]

class SpecialTextBlock(blocks.StructBlock):

    special_text = SpecialTextChooserBlock()
    color = ColorChooserBlock()

    class Meta:
        icon = "pick"
        template = "style/special_text_block.html"

class PaginationSizeBlock(blocks.StructBlock):

    size = SizeChooserBlock(required=False)

    class Meta:
        icon = "view"
        template = "style/button_size_block.html"

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
        icon = "arrow-left"

class DisableBlock(blocks.StructBlock):

    disable = blocks.BooleanBlock(required=False)

    class Meta:
        icon = "tick-inverse"
        template = "style/disable_block.html"

class AddClassBlock(blocks.StructBlock):

    add_class = blocks.CharBlock(required=False)

    class Meta:
        icon = "code"
        template = "style/add_class_block.html"

class AnimationBlock(blocks.StructBlock):

    animation = blocks.ChoiceBlock(choices=[
        ("bounce","bounce"),
        ("flash","flash"),
        ("pulse","pulse"),
        ("rubberBand","rubberBand"),
        ("shakeX","shakeX"),
        ("shakeY","shakeY"),
        ("headShake","headShake"),
        ("swing","swing"),
        ("tada","tada"),
        ("wobble","wobble"),
        ("jello","jello"),
        ("heartBeat","heartBeat"),
        ("backInDown","backInDown"),
        ("backInLeft","backInLeft"),
        ("backInRight","backInRight"),
        ("backInUp","backInUp"),
        ("backOutDown","backOutDown"),
        ("backOutLeft","backOutLeft"),
        ("backOutRight","backOutRight"),
        ("backOutUp","backOutUp"),
        ("bounceIn","bounceIn"),
        ("bounceInDown","bounceInDown"),
        ("bounceInLeft","bounceInLeft"),
        ("bounceInRight","bounceInRight"),
        ("bounceInUp","bounceInUp"),
        ("bounceOut","bounceOut"),
        ("bounceOutDown","bounceOutDown"),
        ("bounceOutLeft","bounceOutLeft"),
        ("bounceOutRight","bounceOutRight"),
        ("bounceOutUp","bounceOutUp"),
        ("fadeIn","fadeIn"),
        ("fadeInDown","fadeInDown"),
        ("fadeInDownBig","fadeInDownBig"),
        ("fadeInLeft","fadeInLeft"),
        ("fadeInLeftBig","fadeInLeftBig"),
        ("fadeInRight","fadeInRight"),
        ("fadeInRightBig","fadeInRightBig"),
        ("fadeInUp","fadeInUp"),
        ("fadeInUpBig","fadeInUpBig"),
        ("fadeInTopLeft","fadeInTopLeft"),
        ("fadeInTopRight","fadeInTopRight"),
        ("fadeInBottomLeft","fadeInBottomLeft"),
        ("fadeInBottomRight","fadeInBottomRight"),
        ("fadeOut","fadeOut"),
        ("fadeOutDown","fadeOutDown"),
        ("fadeOutDownBig","fadeOutDownBig"),
        ("fadeOutLeft","fadeOutLeft"),
        ("fadeOutLeftBig","fadeOutLeftBig"),
        ("fadeOutRight","fadeOutRight"),
        ("fadeOutRightBig","fadeOutRightBig"),
        ("fadeOutUp","fadeOutUp"),
        ("fadeOutUpBig","fadeOutUpBig"),
        ("fadeOutTopLeft","fadeOutTopLeft"),
        ("fadeOutTopRight","fadeOutTopRight"),
        ("fadeOutBottomRight","fadeOutBottomRight"),
        ("fadeOutBottomLeft","fadeOutBottomLeft"),
        ("flip","flip"),
        ("flipInX","flipInX"),
        ("flipInY","flipInY"),
        ("flipOutX","flipOutX"),
        ("flipOutY","flipOutY"),
        ("lightSpeedInRight","lightSpeedInRight"),
        ("lightSpeedInLeft","lightSpeedInLeft"),
        ("lightSpeedOutRight","lightSpeedOutRight"),
        ("lightSpeedOutLeft","lightSpeedOutLeft"),
        ("rotateIn","rotateIn"),
        ("rotateInDownLeft","rotateInDownLeft"),
        ("rotateInDownRight","rotateInDownRight"),
        ("rotateInUpLeft","rotateInUpLeft"),
        ("rotateInUpRight","rotateInUpRight"),
        ("rotateOut","rotateOut"),
        ("rotateOutDownLeft","rotateOutDownLeft"),
        ("rotateOutDownRight","rotateOutDownRight"),
        ("rotateOutUpLeft","rotateOutUpLeft"),
        ("rotateOutUpRight","rotateOutUpRight"),
        ("hinge","hinge"),
        ("jackInTheBox","jackInTheBox"),
        ("rollIn","rollIn"),
        ("rollOut","rollOut"),
        ("zoomIn","zoomIn"),
        ("zoomInDown","zoomInDown"),
        ("zoomInLeft","zoomInLeft"),
        ("zoomInRight","zoomInRight"),
        ("zoomInUp","zoomInUp"),
        ("zoomOut" ,"zoomOut"),
        ("zoomOutDown" ,"zoomOutDown"),
        ("zoomOutLeft" ,"zoomOutLeft"),
        ("zoomOutRight" ,"zoomOutRight"),
        ("zoomOutUp" ,"zoomOutUp"),
        ("slideInDown" ,"slideInDown"),
        ("slideInLeft" ,"slideInLeft"),
        ("slideInRight" ,"slideInRight"),
        ("slideInUp" ,"slideInUp"),
        ("slideOutDown" ,"slideOutDown"),
        ("slideOutLeft" ,"slideOutLeft"),
        ("slideOutRight" ,"slideOutRight"),
        ("slideOutUp" ,"slideOutUp"),
        ], required=True, closed=True)
    delay = blocks.IntegerBlock(min_value=2, max_value=5, required=False, closed=True)
    speed = blocks.ChoiceBlock(choices=[
        ("slow", "slow"),
        ("slower", "slower"),
        ("fast", "fast"),
        ("faster", "faster")], required=False, closed=True)
    repeat = blocks.ChoiceBlock(choices=[
        ("repeat-1", "1"),
        ("repeat-2", "2"),
        ("repeat-3", "3"),
        ("infinite", "infinite")], required=False, closed=True)

    class Meta:
        template = "style/animation_block.html"


# Style blocks :

class LayoutStyleBlock(blocks.StreamBlock):

    # Content :
    background = BackgroundColorBlock(required=False, closed=True)
    text_alignement = TextAlignementBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)

    # Box :
    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    width = SizeWidthChooserBlock(required=False, closed=True)
    height = SizeHeightChooserBlock(required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    display = DisplayChooserBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    shadow = ShadowSizeBlock(required=False, closed=True)

    # Extra :
    add_class = AddClassBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)

class NavbarStyleBlock(blocks.StreamBlock):

    # Content :
    background = BackgroundColorBlock(required=False, closed=True)
    text_alignement = TextAlignementBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)

    # Box :
    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    width = SizeWidthChooserBlock(required=False, closed=True)
    height = SizeHeightChooserBlock(required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    display = DisplayChooserBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    shadow = ShadowSizeBlock(required=False, closed=True)
    fixed = FixedPositionChooserBlock(required=False, closed=True)

    # Extra :
    add_class = AddClassBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)

class TextStyleBlock(blocks.StreamBlock):

    # Text :
    text_color = TextColorBlock(required=False, closed=True)
    text_size = TextSizeBlock(required=False, closed=True)
    font = FontChooserBlock(required=False, closed=True)
    text_overflow = TextOverflowChooserBlock(required=False, closed=True)
    badge = BadgeBlock(required=False, closed=True)

    # Content :
    background = BackgroundColorBlock(required=False, closed=True)
    text_alignement = TextAlignementBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    display = DisplayChooserBlock(required=False, closed=True)

    # Box :
    shadow = ShadowSizeBlock(required=False, closed=True)
    width = SizeWidthChooserBlock(required=False, closed=True)
    height = SizeHeightChooserBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)

    add_class = AddClassBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)

    class Meta:
        icon = "pilcrow"

class ButtonStyleBlock(blocks.StreamBlock):

    disable = DisableBlock(required=False, closed=True)
    size = ButtonSizeBlock(required=False, closed=True)
    color = ButtonColorBlock(required=False, closed=True)
    background = BackgroundColorBlock(required=False, closed=True)
    font = FontChooserBlock(required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    display = DisplayChooserBlock(required=False, closed=True)
    add_class = AddClassBlock(required=False, closed=True)
    shadow = ShadowSizeBlock(required=False, closed=True)
    width = SizeWidthChooserBlock(required=False, closed=True)
    height = SizeHeightChooserBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)

class CarouselStyleBlock(blocks.StreamBlock):

    transitions = blocks.ChoiceBlock(choices=[("carousel-fade", "fade")], required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    add_class = AddClassBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)
    shadow = ShadowSizeBlock(required=False, closed=True)
    width = SizeWidthChooserBlock(required=False, closed=True)
    height = SizeHeightChooserBlock(required=False, closed=True)
    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)

class ImageStyleBlock(blocks.StreamBlock):

    background = BackgroundColorBlock(required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    add_class = AddClassBlock(required=False, closed=True)
    display = DisplayChooserBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)
    shadow = ShadowSizeBlock(required=False, closed=True)
    width = SizeWidthChooserBlock(required=False, closed=True)
    height = SizeHeightChooserBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)

class NavStyleBlock(blocks.StreamBlock):

    size = PaginationSizeBlock(required=False, closed=True)
    background = BackgroundColorBlock(required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    display = DisplayChooserBlock(required=False, closed=True)
    add_class = AddClassBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)
    shadow = ShadowSizeBlock(required=False, closed=True)
    fixed_position = FixedPositionChooserBlock(required=False, closed=True)
    width = SizeWidthChooserBlock(required=False, closed=True)
    height = SizeHeightChooserBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)
