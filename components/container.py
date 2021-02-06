from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock

from .base import *
from .text import *
from .media import *
from .form import *

class PopoverBlock(blocks.StructBlock):

    button = ButtonBlock(required=False, closed=True)
    title = blocks.TextBlock(required=False, closed=True)
    text = blocks.TextBlock(required=False, closed=True)
    placement = blocks.ChoiceBlock(choices = [
        ("left", "left"),
        ("right", "right"),
        ("bottom", "bottom"),
        ("top", "top")], required=True, closed=True)

    class Meta:
        template = "components/container/container/popover_block.html"
        group = "Components"

class TableBlock(blocks.StructBlock):

    table_color = ColorChooserBlock(required=False, closed=True)
    table = TableBlock(required=False, closed=True)

    class Meta:
        template = "components/container/container/table_block.html"
        icon = "list-ol"

class TabBlock(blocks.StructBlock):

    nav = blocks.StreamBlock([
        ("tab", blocks.StructBlock([
            ("label", TitleBlock(required=True, closed=True)),
            ("content", blocks.StreamBlock([
                ("title", TitleBlock(required=False, closed=True)),
                ("paragraph", RichTextBlock(required=False, closed=True)),
                ("quote", QuoteBlock(required=False, closed=True)),
                ("image", ImageBlock(required=False, closed=True)),
                ("html", blocks.RawHTMLBlock(required=False, closed=True)),
                ("button", ButtonBlock(required=False, closed=True)),
                ("popover", PopoverBlock(required=False, closed=True)),
                ("link", LinkBlock(required=False, closed=True)),
            ], required=False, closed=True))
        ], required=False, closed=True)),
    ], required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(required=False, closed=True)

    class Meta:
        template = "components/container/tab_block.html"
        icon = "arrow-right-big"
        group = "Containers"

class ListBlock(blocks.StructBlock):

    rows = blocks.ListBlock(
        blocks.StructBlock([
            ("style", StyleBlock(required=False, closed=True)),
            ("content", blocks.StreamBlock([
                ("title", TitleBlock(required=False, closed=True)),
                ("paragraph", RichTextBlock(required=False, closed=True)),
                ("quote", QuoteBlock(required=False, closed=True)),
                ("link", LinkBlock(required=False, closed=True)),
                ("html", blocks.RawHTMLBlock(required=False, closed=True)),
                ("image", ImageBlock(required=False, closed=True)),
                ("button", ButtonBlock(required=False, closed=True)),
            ], required=False, closed=True)),
        ], required=False, closed=True)
    )
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(required=False, closed=True)

    class Meta:
        icon = "list-ul"
        template = "components/container/list_block.html"
        group = "Containers"

class ContainerBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True, group="Text")),

        ("image", ImageBlock(required=False, closed=True)),
        ("carousel", CarouselBlock(required=False, closed=True)),

        ("button", ButtonBlock(required=False, closed=True)),
        ("form", FormBlock(required=False, closed=True)),
        ("account", AccountFormBlock(required=False, closed=True)),

        ("link", LinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),

        ("tab", TabBlock(required=False, closed=True)),
        ("group", ButtonGroupBlock(required=False, closed=True)),
        ("table", TabBlock(required=False, closed=True)),
        ("list", ListBlock(required=False, closed=True)),

        ("popover", PopoverBlock(required=False, closed=True)),
        ("container", ContainerBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        icon = "grip"
        template = "components/container/container_block.html"
        group = "Containers"

class BannerBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True, group="Text")),

        ("image", ImageBlock(required=False, closed=True)),
        ("carousel", CarouselBlock(required=False, closed=True)),

        ("button", ButtonBlock(required=False, closed=True)),
        ("form", FormBlock(required=False, closed=True)),
        ("account", AccountFormBlock(required=False, closed=True)),

        ("link", LinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),

        ("popover", PopoverBlock(required=False, closed=True)),
        ("container", ContainerBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        icon = "grip"
        template = "components/container/container_block.html"
        group = "Containers"

class ModalBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("header", ContainerBlock(required=False, closed=True)),
        ("body", ContainerBlock(required=False, closed=True)),
        ("footer", ContainerBlock(required=False, closed=True))
    ], required=False, closed=True)
    block = BaseBlock(required=False, closed=True)

    class Meta:
        icon = "image"
        template = "components/container/modal_block.html"
        group = "Containers"

class CardBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("header", TitleBlock(required=False, closed=True)),
        ("image_card", ImageBlock(required=False, closed=True)),
        ("title", TitleBlock(required=False, closed=True)),
        ("subtitle", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
        ("footer", TitleBlock(required=False, closed=True))
    ], required=False, closed=True)
    block = BaseBlock(required=False, closed=True)

    class Meta:
        icon = "image"
        template = "components/container/card_block.html"
        group = "Containers"