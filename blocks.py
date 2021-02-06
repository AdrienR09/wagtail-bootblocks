from wagtail.core import blocks

from .components.base import *
from .components.text import *
from .components.form import *
from .components.nav import *
from .components.media import *
from .components.container import *

class HeaderBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("navbar", NavbarBlock(required=False, closed=True)),
        ("banner", BannerBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        template = "blocks/header_block.html"
        icon = "doc-full-inverse"
        label = "header"

class SectionBlock(blocks.StructBlock):

    content = blocks.StreamBlock([

        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True, group="Text")),

        ("image", ImageBlock(required=False, closed=True)),
        ("carousel", CarouselBlock(required=False, closed=True)),

        ("button", ButtonBlock(required=False, closed=True)),
        ("link", LinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
        ("button_group", ButtonGroupBlock(required=False, closed=True)),

        ("form", FormBlock(required=False, closed=True)),
        ("account", AccountFormBlock(required=False, closed=True)),

        ("nav", NavBlock(required=False, closed=True)),

        ("tab", TabBlock(required=False, closed=True)),
        ("table", TabBlock(required=False, closed=True)),
        ("list", ListBlock(required=False, closed=True)),

        ("popover", PopoverBlock(required=False, closed=True)),
        ("card", CardBlock(required=False, closed=True)),
        ("modal", ModalBlock(required=False, closed=True)),
        ("layout", LayoutBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        template = "blocks/section_block.html"
        icon = "doc-full-inverse"
        label = "section"

class AsideBlock(blocks.StructBlock):

    content = blocks.StreamBlock([

        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True, group="Text")),

        ("image", ImageBlock(required=False, closed=True)),
        ("carousel", CarouselBlock(required=False, closed=True)),

        ("button", ButtonBlock(required=False, closed=True)),
        ("link", LinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
        ("button_group", ButtonGroupBlock(required=False, closed=True)),

        ("form", FormBlock(required=False, closed=True)),
        ("account", AccountFormBlock(required=False, closed=True)),

        ("nav", NavBlock(required=False, closed=True)),

        ("tab", TabBlock(required=False, closed=True)),
        ("table", TabBlock(required=False, closed=True)),
        ("list", ListBlock(required=False, closed=True)),

        ("popover", PopoverBlock(required=False, closed=True)),
        ("card", CardBlock(required=False, closed=True)),
        ("modal", ModalBlock(required=False, closed=True)),
        ("layout", LayoutBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        template = "blocks/aside_block.html"
        icon = "doc-full-inverse"
        label = "aside"

class FooterBlock(blocks.StructBlock):

    content = blocks.StreamBlock([

        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True, group="Text")),

        ("image", ImageBlock(required=False, closed=True)),
        ("carousel", CarouselBlock(required=False, closed=True)),

        ("button", ButtonBlock(required=False, closed=True)),
        ("link", LinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
        ("button_group", ButtonGroupBlock(required=False, closed=True)),

        ("form", FormBlock(required=False, closed=True)),
        ("account", AccountFormBlock(required=False, closed=True)),

        ("nav", NavBlock(required=False, closed=True)),

        ("tab", TabBlock(required=False, closed=True)),
        ("table", TabBlock(required=False, closed=True)),
        ("list", ListBlock(required=False, closed=True)),

        ("popover", PopoverBlock(required=False, closed=True)),
        ("card", CardBlock(required=False, closed=True)),
        ("modal", ModalBlock(required=False, closed=True)),
        ("layout", LayoutBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = ContainerBaseBlock(required=False, closed=True)

    class Meta:
        template = "blocks/footer_block.html"
        icon = "doc-full-inverse"
        label = "footer"
