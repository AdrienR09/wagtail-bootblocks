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
        template = "style/margin_block.html"
        group = "dimension"

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
        template = "style/padding_block.html"
        group = "dimension"

class WidthChooserBlock(blocks.ChoiceBlock):

    choices = [
        ("auto" , "auto"),
        ("w-25" , "25%"),
        ("w-50" , "50%"),
        ("w-75" , "75%"),
        ("w-100" , "100%"),
    ]

    class Meta:
        icon = "arrow-down"
        group = "dimension"

class HeightChooserBlock(blocks.ChoiceBlock):

    choices = [
        ("auto" , "auto"),
        ("h-25" , "25%"),
        ("h-50" , "50%"),
        ("h-75" , "75%"),
        ("h-100" , "100%"),
    ]

    class Meta:
        icon = "arrow-up"
        group = "dimension"

class DimensionBlock(blocks.StructBlock):

    height = blocks.IntegerBlock(min_value=1, max_value=500, required=False)
    width = blocks.IntegerBlock(min_value=1, max_value=500, required=False)

    class Meta:
        icon = "arrows-up-down"
        template = "style/dimension_block.html"
        group = "dimension"

class PositionChooserBlock(blocks.ChoiceBlock):
    choices = [
        ("fixed-left", "fixed-left"),
        ("fixed-top", "fixed-top"),
        ("fixed-bottom", "fixed-bottom"),
        ("fixed-right", "fixed-right"),
        ("sticky-left", "sticky-left"),
        ("sticky-top", "sticky-top"),
        ("sticky-bottom", "sticky-bottom"),
        ("sticky-right", "sticky-right"),
    ]

    class Meta:
        icon = "arrow-left"
        group = "layout"

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
        group = "layout"
        template = "style/display_block.html"

class LayoutChooserBlock(blocks.ChoiceBlock):

    choices =[
        ("row", "row"),
        ("container", "container"),
        ("jumbotron", "jumbotron"),
    ]

    class Meta:
        icon = "spinner"
        group = "layout"

class ColumnsBlock(blocks.StructBlock):

    columns = blocks.IntegerBlock(min_value=0, max_value=12, required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "grip"
        group = "layout"
        template = "style/column_block.html"

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
        group = "layout"
        template = "style/flex_block.html"

class FloatBlock(blocks.StructBlock):
    type = blocks.ChoiceBlock(choices=[
        ("left", "left"),
        ("right", "right"),
        ("none", "none"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "spinner"
        group = "layout"
        template = "style/float_block.html"

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
        group = "alignement"
        template = "style/horizontal_alignement_block.html"

class VerticalAlignementBlock(blocks.StructBlock):

    alignement = blocks.ChoiceBlock(choices = [
        ("start", "start"),
        ("center", "center"),
        ("end", "end"),
        ("stretch", "stretch"),
        ("baseline", "baseline"),
    ], required=False, closed=True)
    item = blocks.ChoiceBlock(choices = [
        ("items", "items"),
        ("self", "self"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "arrow-up"
        group = "alignement"
        template = "style/vertical_alignement_block.html"

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
        group = "alignement"
        template = "style/text_alignement_block.html"

class BackgroundColorBlock(blocks.StructBlock):

    background_color = ColorChooserBlock(required=False)

    class Meta:
        icon = "snippet"
        template = "style/background_color_block.html"
        group = "content"

class ShadowSizeBlock(blocks.StructBlock):

    size = SizeChooserBlock(required=False, closed=True)
    gradient = blocks.BooleanBlock(required=False, closed=True)

    class Meta:
        icon = "view"
        template = "style/shadow_block.html"
        group = "content"

class BorderBlock(blocks.StructBlock):

    border_style = blocks.ChoiceBlock(choices = [
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
    border_shape = blocks.ChoiceBlock(choices = [
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
        template = "style/border_block.html"
        group = "content"

# Text blocks :

class FontChooserBlock(blocks.ChoiceBlock):

    choices = [
        ("first-font", "first-font"),
        ("second-font", "second-font"),
        ("third-font", "third-font"),
    ]

    class Meta:
        icon = "pilcrow"
        group = "text"

class TextSizeBlock(blocks.ChoiceBlock):
    
    choices = [
        ("display-1", "display-1"),
        ("display-2", "display-2"),
        ("display-3", "display-3"),
        ("display-4", "display-4"),
        ("display-5", "display-5"),
        ("display-6", "display-6"),
    ]

    class Meta:
        icon = "arrows-up-down"
        group = "text"

class TextColorBlock(blocks.StructBlock):

    text_color = ColorChooserBlock()

    class Meta:
        icon = "snippet"
        template = "style/text_color_block.html"
        group = "text"

class TextOverflowChooserBlock(blocks.ChoiceBlock):

    choices = [
        ("text-break", "break"),
        ("text-truncate", "truncate"),
        ("text-wrap", "wrap"),
        ("text-nowrap", "nowrap"),
    ]

    class Meta:
        icon = "redirect"
        group = "text"

class SpecialTextBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices=[
        ("alert", "alert"),
        ("badge", "badge"),
    ], required=True, closed=True)
    color = ColorChooserBlock(required=True, closed=True)

    class Meta:
        icon = "pick"
        group = "text"
        template = "style/special_text_block.html"

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
        template = "style/modal_style_block.html"

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

# Other :

class PaginationSizeBlock(blocks.StructBlock):

    size = SizeChooserBlock(required=False)

    class Meta:
        icon = "view"
        group = "special"
        template = "style/button_size_block.html"

class AddClassBlock(blocks.StructBlock):

    add_class = blocks.CharBlock(required=False)

    class Meta:
        icon = "code"
        template = "style/add_class_block.html"
        group = "special"

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
        group = "special"


# Style blocks :

class StyleBlock(blocks.StreamBlock):

    margin = MarginBlock(required=False, closed=True)
    padding = PaddingBlock(required=False, closed=True)
    width = WidthChooserBlock(required=False, closed=True)
    height = HeightChooserBlock(required=False, closed=True)
    position = PositionChooserBlock(required=False, closed=True)
    layout = LayoutChooserBlock(required=False, closed=True)
    display = DisplayBlock(required=False, closed=True)
    columns = ColumnsBlock(required=False, closed=True)
    flex = FlexBlock(required=False, closed=True)
    floating = FloatBlock(required=False, closed=True)
    text_alignement = TextAlignementBlock(required=False, closed=True)
    horizontal_alignement = HorizontalAlignementBlock(required=False, closed=True)
    vertical_alignement = VerticalAlignementBlock(required=False, closed=True)
    background = BackgroundColorBlock(required=False, closed=True)
    border = BorderBlock(required=False, closed=True)
    shadow = ShadowSizeBlock(required=False, closed=True)
    text_color = TextColorBlock(required=False, closed=True)
    text_size = TextSizeBlock(required=False, closed=True)
    font = FontChooserBlock(required=False, closed=True)
    text_overflow = TextOverflowChooserBlock(required=False, closed=True)
    badge = SpecialTextBlock(required=False, closed=True)
    button_color = ButtonColorBlock(required=False, closed=True)
    modal = ModalStyleBlock(required=False, closed=True)
    button_size = ButtonSizeBlock(required=False, closed=True)
    add_class = AddClassBlock(required=False, closed=True)
    animation = AnimationBlock(required=False, closed=True)