from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

from stream.style import *

# Text Block :

class TitleBlock(blocks.StructBlock):

    choices = [
        ("display-1", "Title"),
        ("display-3", "SubTitle"),
        ("h1", "H1"),
        ("h2", "H2"),
        ("h3", "H3"),
        ("h4", "H4"),
        ("h5", "H5"),
    ]

    title = blocks.CharBlock(required=True, max_length=100)
    level = blocks.ChoiceBlock(required=True, choices=choices)
    style = blocks.StreamBlock([
        ("text_color", ColorChooserBlock()),
        ("background_color", ColorChooserBlock()),
        ("text_alignement", TextAlignementChooserBlock()),
        ("vertical_alignement", VerticalAlignementChooserBlock()),
        ("horizontal_alignement", HorizontalAlignementChooserBlock()),
        ("columns", GridChooserBlock()),
        ("shadow", ShadowChooserBlock()),
        ("margin", MarginBlock()),
        ("padding", PaddingBlock()),
        ("border", BorderBlock()),
    ], required=False, closed=True)

    class Meta:
        template = "blocks/title_block.html"
        icon = "title"

class ParagraphBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(required=True)
    style = blocks.StreamBlock([
        ("text_color", ColorChooserBlock()),
        ("text_style", TextStyleChooserBlock()),
        ("background_color", ColorChooserBlock()),
        ("text_alignement", TextAlignementChooserBlock()),
        ("vertical_alignement", VerticalAlignementChooserBlock()),
        ("horizontal_alignement", HorizontalAlignementChooserBlock()),
        ("columns", GridChooserBlock()),
        ("shadow", ShadowChooserBlock()),
        ("margin", MarginBlock()),
        ("padding", PaddingBlock()),
        ("border", BorderBlock()),
    ], required=False, closed=True)

    class Meta:
        template = "blocks/paragraph_block.html"
        icon = "pilcrow"

class QuoteBlock(blocks.StructBlock):

    quote = blocks.RichTextBlock(required=True)
    author = blocks.CharBlock(max_length=200, required=False)
    style = blocks.StreamBlock([
        ("text_color", ColorChooserBlock()),
        ("background_color", ColorChooserBlock()),
        ("text_alignement", TextAlignementChooserBlock()),
        ("vertical_alignement", VerticalAlignementChooserBlock()),
        ("horizontal_alignement", HorizontalAlignementChooserBlock()),
        ("columns", GridChooserBlock()),
        ("shadow", ShadowChooserBlock()),
        ("margin", MarginBlock()),
        ("padding", PaddingBlock()),
        ("border", BorderBlock()),
    ], required=False, closed=True)

    class Meta:
        template = "blocks/quote_block.html"
        icon = "openquote"

class TableBlock(blocks.StructBlock):

    table_color = ColorChooserBlock(required=False)
    table = TableBlock()

    class Meta:
        template = "blocks/table_block.html"
        icon = "list-ol"

class ButtonStructValue(blocks.StructValue):

    def url(self):
        page = self.get('page')
        link = self.get('link')
        if page:
            return page
        elif link:
            return link
        return None

class ButtonBlock(blocks.StructBlock):

    label = blocks.CharBlock(required=False, max_length=100)
    page = blocks.PageChooserBlock(required=False)
    link = blocks.URLBlock(required=False)
    style = blocks.StreamBlock([
        ("button_color", ColorChooserBlock()),
        ("text_color", ColorChooserBlock()),
        ("button_size", blocks.ChoiceBlock(required=False, choices=[
        ('btn-sm', 'Small'),
        ('', 'Regular'),
        ('btn-lg', 'Large'),], icon='arrows-up-down')),
        ("button_outlined", ColorChooserBlock()),
        ("button_disabled", blocks.BooleanBlock()),
        ("margin", MarginBlock()),
        ("padding", PaddingBlock()),
        ("shadow", ShadowChooserBlock()),
        ("border", BorderBlock()),
    ], required=False, closed=True)

    class Meta:
        template = "blocks/button_block.html"
        icon = "tick"
        value_class = ButtonStructValue

class CardBlock(blocks.StructBlock):

    content = blocks.StreamBlock([
        ("en_tête", TitleBlock(required=False)),
        ("titre", TitleBlock(required=False, related_name="title")),
        ("sous_titre", TitleBlock(required=False, related_name="subtitle")),
        ("paragraphe", ParagraphBlock(required=False)),
        ("image", ImageChooserBlock(required=False)),
        ("bouton", ButtonBlock(required=False)),
        ("pied_de_page", TitleBlock(required=False)),
    ], required=False, closed=True)
    style = blocks.StreamBlock([
        ("card_color", ColorChooserBlock()),
        ("text_alignement", TextAlignementChooserBlock()),
        ("vertical_alignement", VerticalAlignementChooserBlock()),
        ("horizontal_alignement", HorizontalAlignementChooserBlock()),
        ("columns", GridChooserBlock()),
        ("shadow", ShadowChooserBlock()),
        ("margin", MarginBlock()),
        ("padding", PaddingBlock()),
        ("border", BorderBlock()),
    ], required=False, closed=True)

    class Meta:
        icon = "form"
        template = "blocks/card_block.html"

class BannerBlock(blocks.StructBlock):

    background = ImageChooserBlock(required=False)
    content = blocks.StreamBlock([
        ("header", TitleBlock(required=False)),
        ("title", TitleBlock(required=False, related_name="title")),
        ("subtitle", TitleBlock(required=False, related_name="subtitle")),
        ("text", ParagraphBlock(required=False)),
        ("image", ImageChooserBlock(required=False)),
        ("button", ButtonBlock(required=False)),
        ("footer", TitleBlock(required=False)),
    ], required=False, closed=True)
    style = blocks.StreamBlock([
        ("extra_dimension", ExtraDimensionBlock()),
        ("text_alignement", TextAlignementChooserBlock()),
        ("vertical_alignement", VerticalAlignementChooserBlock()),
        ("horizontal_alignement", HorizontalAlignementChooserBlock()),
        ("columns", GridChooserBlock()),
        ("shadow", ShadowChooserBlock()),
        ("margin", MarginBlock()),
        ("padding", PaddingBlock()),
        ("border", BorderBlock()),
    ], required=False, closed=True)

    class Meta:
        icon = "form"
        template = "blocks/banner_block.html"
        label = "card"


class ContainerBlock(blocks.StructBlock):

    container_type = ContainerChooserBlock(required=False)
    background = ImageChooserBlock(required=False)
    content = blocks.StreamBlock(
        [
            ("Titre", TitleBlock()),
            ("Paragraphe", ParagraphBlock()),
            ("Citation", QuoteBlock()),
            ("Table", TableBlock()),
            ("Boutton", ButtonBlock()),
            ("Card", CardBlock()),
            ("Image", ImageChooserBlock()),
        ], required=False, closed=True)
    style = blocks.StreamBlock([
        ("extra_dimension", ExtraDimensionBlock()),
        ("dimension", DimensionBlock()),
        ("text_alignement", TextAlignementChooserBlock()),
        ("vertical_alignement", VerticalAlignementChooserBlock()),
        ("horizontal_alignement", HorizontalAlignementChooserBlock()),
        ("columns", GridChooserBlock()),
        ("shadow", ShadowChooserBlock()),
        ("margin", MarginBlock()),
        ("padding", PaddingBlock()),
        ("border", BorderBlock()),
    ], required=False, closed=True)

    class Meta:
        icon = "form"
        template = "blocks/container_block.html"