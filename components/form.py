from wagtail.core import blocks

from .base import *
from .text import *
from .media import *
from .button import *


class LabelBlock(blocks.StructBlock):
    
    text = blocks.CharBlock(required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
    ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "components/form/label_block.html"
        icon = "pill"

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
    text = blocks.CharBlock(required=False, closed=True)
    label = LabelBlock(required=False, closed=True)
    info = TextBlock(required=False, closed=True)
    block = InputBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/form/input_block.html"

class SelectFormBlock(blocks.StructBlock):

    name = blocks.CharBlock(required=True, closed=True)
    options = blocks.ListBlock(blocks.CharBlock(required=True, closed=True))
    label = LabelBlock(required=False, closed=True)
    info = TextBlock(required=False, closed=True)
    block = SelectBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/form/select_block.html"

class TextAreaFormBlock(blocks.StructBlock):

    name = blocks.CharBlock(required=True, closed=True)
    text = blocks.CharBlock(required=False, closed=True)
    label = LabelBlock(required=False, closed=True)
    info = TextBlock(required=False, closed=True)
    block = InputBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/form/textarea_block.html"

class LegendBlock(blocks.StructBlock):

    text = blocks.TextBlock(required=False, closed=True)
    block = BaseBlock(required=False, closed=True)

    class Meta:
        template = "components/form/legend_block.html"

class SubmitBlock(blocks.StructBlock):

    text = TitleBlock(required=False, closed=True)
    tooltip = TooltipBlock(required=False, closed=True)
    block = ButtonBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/form/submit_block.html"
        icon = "tick"

class FormBlock(blocks.StructBlock):

    page = blocks.PageChooserBlock(required=False, closed=True)
    link = blocks.CharBlock(required=False, closed=True)
    content = blocks.StreamBlock([
        ("input", InputFormBlock(required=False, closed=True)),
        ("select", SelectFormBlock(required=False, closed=True)),
        ("textarea", TextAreaFormBlock(required=False, closed=True)),
        ("legend", LegendBlock(required=False, closed=True)),
        ("submit", SubmitBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = FormBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/form/form_block.html"
        icon = "form"
        value_class = URLStructValue
        group = "form"

class AccountFormBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices=[
        ("signup", "signup"),
        ("login", "login"),
        ("logout", "logout"),
        ("reset_password", "reset_password"),
        ("change_password", "change_password"),
        ("confirm_email", "confirm_email"),
    ])
    content = blocks.StreamBlock([
        ("input", InputFormBlock(required=False, closed=True)),
        ("legend", LegendBlock(required=False, closed=True)),
        ("submit", SubmitBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = FormBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/form/account_form_block.html"
        icon = "form"
        group = "form"
