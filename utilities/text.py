from wagtail.core import blocks

from .color import *

class FontChooserBlock(blocks.ChoiceBlock):
    choices = [
        ("first-font", "first-font"),
        ("second-font", "second-font"),
        ("third-font", "third-font"),
    ]

    class Meta:
        icon = "pilcrow"
        group = "text"

class TextSizeChooserBlock(blocks.ChoiceBlock):
    choices = [
        ("fs-1", "size-1"),
        ("fs-2", "size-2"),
        ("fs-3", "size-3"),
        ("fs-4", "size-4"),
        ("fs-5", "size-5"),
        ("fs-6", "size-6"),
    ]

    class Meta:
        icon = "arrows-up-down"
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
        template = "components/style/special_text_block.html"

class FontWeightChooserBlock(blocks.ChoiceBlock):
    choices = [
        ("fw-bold", "bold"),
        ("fw-bolder", "bolder"),
        ("fw-normal", "normal"),
        ("fw-light", "light"),
        ("fw-lighter", "lighter"),
        ("fst-italic", "italic"),
        ("fw-bolder", "bolder"),
    ]

    class Meta:
        icon = "redirect"
        group = "text"

class TextDecorationChooserBlock(blocks.ChoiceBlock):
    choices = [
        ("text-decoration-underline", "underline"),
        ("text-decoration-line-through", "line-through"),
        ("text-decoration-none", "none"),
    ]

    class Meta:
        icon = "redirect"
        group = "text"

class TextAlignementBlock(blocks.StructBlock):
    alignement = blocks.ChoiceBlock(choices=[
        ("left", "left"),
        ("right", "right"),
        ("center", "center"),
        ("justify", "justify"),
    ], required=False, closed=True)
    breakpoints = BreakpointChooserBlock(required=False, closed=True)

    class Meta:
        icon = "horizontalrule"
        group = "layout"
        template = "utilities/text/text_alignement_block.html"

class TextBlock(blocks.StreamBlock):

    font = FontChooserBlock(required=False, closed=True)
    size = TextSizeChooserBlock(required=False, closed=True)
    weight = FontWeightChooserBlock(required=False, closed=True)
    decoration = TextDecorationChooserBlock(required=False, closed=True)
    overflow = TextOverflowChooserBlock(required=False, closed=True)
    special = SpecialTextBlock(required=False, closed=True)
    text_alignement = TextAlignementBlock(required=False, closed=True)

    class Meta:
        group = "text"
        icon = "text"
