from wagtail.core import blocks

from .base import BaseBlock

class TitleBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False, closed=True)
    level = blocks.ChoiceBlock(choices= [
        ("p", "standard"),
        ("h1", "H1"),
        ("h2", "H2"),
        ("h3", "H3"),
        ("h4", "H4"),
        ("h5", "H5"),
    ], required=False, closed=True)
    block = BaseBlock(required=False, closed=True)

    class Meta:
        template = "components/text/title_block.html"
        icon = "title"
        group = "Text"

class TextBlock(blocks.StructBlock):

    text = blocks.TextBlock(required=False, closed=True)
    block = BaseBlock(required=False, closed=True)

    class Meta:
        template = "components/text/text_block.html"
        icon = "pilcrow"
        group = "Text"

class RichTextBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(required=False, closed=True)
    block = BaseBlock(required=False, closed=True)

    class Meta:
        template = "components/text/text_block.html"
        icon = "pilcrow"
        group = "Text"

class QuoteBlock(blocks.StructBlock):

    quote = blocks.RichTextBlock(required=False, closed=True)
    author = blocks.CharBlock(max_length=200, required=False, closed=True)
    block = BaseBlock(required=False, closed=True)

    class Meta:
        template = "components/text/quote_block.html"
        icon = "openquote"
        group = "Text"