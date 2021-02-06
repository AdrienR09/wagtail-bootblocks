from wagtail.core import blocks

from .base import *
from .text import *
from .media import *

class URLStructValue(blocks.StructValue):

    def url(self):
        page = self.get('page')
        link = self.get('link')
        if page:
            return page.url
        elif link:
            return link
        else:
            return None

class TooltipBlock(blocks.StructBlock):

    title = blocks.TextBlock(required=False, closed=True)
    placement = blocks.ChoiceBlock(choices=[
        ("left", "left"),
        ("right", "right"),
        ("bottom", "bottom"),
        ("top", "top")], required=False, closed=True)

class ButtonBlock(blocks.StructBlock):

    page = blocks.PageChooserBlock(required=False, closed=True)
    link = blocks.CharBlock(required=False, closed=True)
    text = TitleBlock(required=False, closed=True)
    tooltip = TooltipBlock(required=False, closed=True)
    block = ButtonBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/button/button_block.html"
        icon = "tick"
        value_class = URLStructValue
        group = "button"

class LinkBlock(blocks.StructBlock):

    page = blocks.PageChooserBlock(required=False, closed=True)
    link = blocks.CharBlock(required=False, closed=True)
    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("text", TextBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/button/link_block.html"
        icon = "tick"
        value_class = URLStructValue
        group = "button"

class DividerBlock(blocks.StaticBlock):

    class Meta:
        template = "components/button/divider_block.html"
        icon = "tick"

class DropdownButtonBlock(blocks.StructBlock):

    button = ButtonBlock(required=False, closed=True)
    nav = blocks.StreamBlock([
        ("link", LinkBlock(required=False, closed=True)),
        ("divider", DividerBlock(required=False, closed=True)),
    ], required=False, closed=True)
    list = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/button/dropdown_button_block.html"
        icon = "tick"
        group = "button"

class ButtonGroupBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices = [
        ("btn-block", "Button block"),
        ("btn-group", "Button group"),
        ("btn-group btn-group-toggle", "Button group toggle"),
        ("btn-group-vertical", "Button group vertical"),
        ("btn-toolbar", "Button toolbar"),
    ], required=False, closed=True)
    content = blocks.StreamBlock([
        ("button", ButtonBlock(required=False, closed=True)),
        ("link", LinkBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/button/button_group_block.html"
        icon = "grip"
        group = "button"