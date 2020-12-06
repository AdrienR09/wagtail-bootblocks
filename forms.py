from django.forms import CheckboxSelectMultiple

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

from bootblocks.style import *

class InputFormBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices=[
        ("button", "button"),
        ("checkbox", "checkbox"),
        ("color", "color"),
        ("date", "date"),
        ("datetime-local", "datetime-local"),
        ("email", "email"),
        ("file", "file"),
        ("image", "image"),
        ("month", "month"),
        ("number", "number"),
        ("password", "password"),
        ("radio ", "radio "),
        ("range", "range"),
        ("reset", "reset"),
        ("search", "search"),
        ("submit", "submit"),
        ("tel", "tel"),
        ("text", "text"),
        ("time", "time"),
        ("url", "url"),
        ("week", "week"),
    ], required=True, closed=True)
    name = blocks.CharBlock(required=True, closed=True)
    label = blocks.CharBlock(required=False, closed=True)
    value = blocks.CharBlock(required=False, closed=True)
    info = blocks.CharBlock(required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "forms/input_block.html"

class SelectFormBlock(blocks.StructBlock):

    name = blocks.CharBlock(required=True, closed=True)
    label = blocks.CharBlock(required=False, closed=True)
    value = blocks.CharBlock(required=False, closed=True)
    options = blocks.ListBlock(blocks.CharBlock(required=True, closed=True))
    info = blocks.CharBlock(required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "forms/select_block.html"

class TextAreaFormBlock(blocks.StructBlock):

    name = blocks.CharBlock(required=True, closed=True)
    label = blocks.CharBlock(required=False, closed=True)
    value = blocks.CharBlock(required=False, closed=True)
    info = blocks.CharBlock(required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "forms/textarea_block.html"

class LegendBlock(blocks.StructBlock):

    label = blocks.CharBlock(required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "forms/legend_block.html"

class SubmitBlock(blocks.StructBlock):

    label = blocks.CharBlock(required=False, closed=True)
    info = blocks.CharBlock(required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(required=False, closed=True)

    class Meta:
        template = "forms/submit_block.html"
        icon = "tick"
