from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

from bootblocks.style import *
from bootblocks.components import *

class HeaderBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("navbar", NavbarBlock(required=False, closed=True)),
        ("banner", LayoutBlock(required=False, closed=True)),
    ], required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(required=False, closed=True)

    class Meta:
        template = "blocks/header_block.html"
        icon = "doc-full-inverse"
        label = "header"

class ContentBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
        ("popover", PopoverBlock(required=False, closed=True)),
        ("link", LinkBlock(required=False, closed=True)),
        ("tab", TabBlock(required=False, closed=True)),
        ("nav", NavBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
        ("group", ButtonGroupBlock(required=False, closed=True)),
        ("table", TabBlock(required=False, closed=True)),
        ("list", ListBlock(required=False, closed=True)),
        ("card", CardBlock(required=False, closed=True)),
        ("layout", LayoutBlock(required=False, closed=True)),
        ("carousel", CarouselBlock(required=False, closed=True)),
    ], required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(required=False, closed=True)

    class Meta:
        template = "blocks/content_block.html"
        icon = "doc-full-inverse"
        label = "content"

class AsideBlock(ContentBlock):

    class Meta:
        template = "blocks/aside_block.html"
        icon = "doc-full-inverse"
        label = "aside"

class SectionBlock(ContentBlock):

    class Meta:
        template = "blocks/section_block.html"
        icon = "doc-full-inverse"
        label = "section"

class MainBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("content", ContentBlock(required=False, closed=True)),
        ("section", SectionBlock(required=False, closed=True)),
        ("aside", AsideBlock(required=False, closed=True)),
    ], required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(required=False, closed=True)

    class Meta:
        template = "blocks/main_block.html"
        icon = "doc-full-inverse"
        label = "body"

class FooterBlock(ContentBlock):

    class Meta:
        template = "blocks/footer_block.html"
        icon = "doc-full-inverse"
        label = "footer"
