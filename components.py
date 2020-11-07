from django.forms import CheckboxSelectMultiple

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

from bootblocks.style import *

# Text components :

class TitleBlock(blocks.StructBlock):

    choices = [
        ("p", "standard"),
        ("h1", "H1"),
        ("h2", "H2"),
        ("h3", "H3"),
        ("h4", "H4"),
        ("h5", "H5"),
    ]

    title = blocks.CharBlock(max_length=100, required=False, closed=True)
    level = blocks.ChoiceBlock(choices=choices, required=False, closed=True)
    style = TextStyleBlock(closed=True, required=False)

    class Meta:
        template = "components/title_block.html"
        icon = "title"
        group = "Text"

class TextBlock(blocks.StructBlock):

    text = blocks.TextBlock(required=False, closed=True)
    style = TextStyleBlock(closed=True, required=False)

    class Meta:
        template = "components/richtext_block.html"
        icon = "pilcrow"
        group = "Text"

class RichTextBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(required=False, closed=True)
    style = TextStyleBlock(closed=True, required=False)

    class Meta:
        template = "components/richtext_block.html"
        icon = "pilcrow"
        group = "Text"

class QuoteBlock(blocks.StructBlock):

    quote = blocks.RichTextBlock(required=False, closed=True)
    author = blocks.CharBlock(max_length=200, required=False, closed=True)
    style = TextStyleBlock(required=False, closed=True)

    class Meta:
        template = "components/quote_block.html"
        icon = "openquote"
        group = "Text"

# Image components :

class ImageBlock(blocks.StructBlock):

    choices = [
        ("80x80", "80x80"),
        ("100x100", "100x100"),
        ("150x150", "150x150"),
        ("200x200", "200x200"),
        ("300x300", "300x300"),
        ("400x400", "400x400"),
        ("600x600", "600x600"),
        ("600x400", "600x400"),
        ("800x400", "800x400"),
        ("400x600", "400x600"),
        ("400x800", "400x800"),
        ("1200x600", "1200x600"),
        ("1510x600", "1510x600"),
        ("1800x800", "1800x800"),
        ("2000x800", "2000x800"),
        ("1700x1700", "1700x1700"),
    ]

    image = ImageChooserBlock(required=False, closed=True)
    dimensions = blocks.ChoiceBlock(choices=choices, closed=True, required=False)
    style = ImageStyleBlock(closed=True, required=False)

    class Meta:
        template = "components/image_block.html"
        icon = "image"
        group = "Media"

# Form components :

class TooltipBlock(blocks.StructBlock):

    title = blocks.TextBlock(required=False, closed=True)
    placement = blocks.ChoiceBlock(choices=[
        ("left", "left"),
        ("right", "right"),
        ("bottom", "bottom"),
        ("top", "top")], required=False, closed=True)

class LinkStructValue(blocks.StructValue):

    def url(self):
        page = self.get('blocks')
        link = self.get('link')
        if page:
            return page
        elif link:
            return link
        else:
            return None

class ButtonBlock(blocks.StructBlock):

    page = blocks.PageChooserBlock(required=False, closed=True)
    link = blocks.CharBlock(required=False, closed=True)
    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("text", TextBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
    ], required=False, closed=True)
    tooltip = TooltipBlock(required=False, closed=True)
    style = ButtonStyleBlock(required=False, closed=True)

    class Meta:
        template = "components/button_block.html"
        icon = "tick"
        value_class = LinkStructValue
        group = "Form"

class LinkBlock(blocks.StructBlock):

    page = blocks.PageChooserBlock(required=False, closed=True)
    link = blocks.CharBlock(required=False, closed=True)
    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("text", TextBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
    ], required=False, closed=True)

    class Meta:
        template = "components/link_block.html"
        icon = "tick"
        value_class = LinkStructValue
        group = "Form"

class FormBlock(blocks.StructBlock):
    pass

# Nav components :

class DropdownButtonBlock(blocks.StructBlock):

    button = ButtonBlock(required=False, closed=True)
    nav = blocks.StreamBlock([
        ("link", LinkBlock(required=False, closed=True)),
        ("divider", blocks.StaticBlock(required=False, closed=True)),
    ], required=False, closed=True)

    class Meta:
        template = "components/dropdown_button_block.html"
        icon = "tick"
        group = "Navs"

class NavBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices=[
                ("navbar-nav", "Nav"),
                ("nav pills", "Pills"),
                ("breadcrumb", "Breadcrumb"),
                ("pagination", "Pagination"),
    ], required=False, closed=True)
    nav = blocks.StreamBlock([
        ("link", LinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
    ], required=False, closed=True)
    style = LayoutStyleBlock(required=False, closed=True)

    class Meta:
        template = "components/nav_block.html"
        icon = "arrow-right-big"
        group = "Navs"

class NavbarBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices=[
                ("", "None"),
                ("navbar-light", "Light"),
                ("navbar-dark", "Dark"),
    ], required=False, closed=True)
    nav = blocks.StreamBlock([
        ("nav", NavBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
        ("dropdown", ButtonBlock(required=False, closed=True)),
        ("text", RichTextBlock(required=False, closed=True)),
    ], required=False, closed=True)
    expand = BreakpointChooserBlock()
    style = NavbarStyleBlock(required=False, closed=True)

    class Meta:
        template = "components/navbar_block.html"
        icon = "arrow-up-big"

# Extra components :

class PopoverBlock(blocks.StructBlock):

    name = TitleBlock(required=False, closed=True)
    title = blocks.TextBlock(required=False, closed=True)
    text = blocks.TextBlock(required=False, closed=True)
    placement = blocks.ChoiceBlock(choices = [
        ("left", "left"),
        ("right", "right"),
        ("bottom", "bottom"),
        ("top", "top")], required=True, closed=True)
    style = ButtonStyleBlock(required=False, closed=True)

    class Meta:
        template = "components/popover_block.html"
        group = "Components"

class TableBlock(blocks.StructBlock):

    table_color = ColorChooserBlock(required=False, closed=True)
    table = TableBlock(required=False, closed=True)

    class Meta:
        template = "components/table_block.html"
        icon = "list-ol"

class AlertBlock(blocks.StructBlock):
    pass

class ButtonGroupBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices = [
        ("", "None"),
        ("btn-block", "Button block"),
        ("btn-group", "Button group"),
        ("btn-group btn-group-toggle", "Button group toggle"),
        ("btn-group-vertical", "Button group vertical"),
        ("btn-toolbar", "Button toolbar"),
    ], required=False, closed=True)
    content = blocks.StreamBlock([
        ("button", ButtonBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
    ], required=False, colsed=True)
    style = LayoutStyleBlock(required=False, closed=True)

    class Meta:
        template = "components/button_group_block.html"
        icon = "grip"
        group = "Components"

# Container components :

class TabBlock(blocks.StructBlock):

    style = LayoutStyleBlock(required=False, closed=True)
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
    style = LayoutStyleBlock(required=False, closed=True)

    class Meta:
        template = "components/tab_block.html"
        icon = "arrow-right-big"
        group = "Containers"

class ListBlock(blocks.StructBlock):

    style = LayoutStyleBlock(required=False, closed=True)
    rows = blocks.ListBlock(
        blocks.StructBlock([
            ("style", LayoutStyleBlock(required=False, closed=True)),
            ("content", blocks.StreamBlock([
                ("title", TitleBlock(required=False, closed=True)),
                ("paragraph", RichTextBlock(required=False, closed=True)),
                ("quote", QuoteBlock(required=False, closed=True)),
                ("html", blocks.RawHTMLBlock(required=False, closed=True)),
                ("image", ImageBlock(required=False, closed=True)),
                ("button", ButtonBlock(required=False, closed=True)),
            ], required=False, closed=True)),
        ], required=False, closed=True)
    )

    class Meta:
        icon = "list-ul"
        template = "components/list_block.html"
        group = "Containers"

class CardBlock(blocks.StructBlock):

    style = LayoutStyleBlock(required=False, closed=True)
    header = TitleBlock(required=False, closed=True)
    card_image = ImageBlock(required=False, closed=True)
    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("subtitle", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
    ], required=False, closed=True)
    footer = TitleBlock(required=False, closed=True)

    class Meta:
        icon = "image"
        template = "components/card_block.html"
        group = "Containers"

class LayoutBlock3(blocks.StructBlock):

    container_type = blocks.ChoiceBlock([
        ("", "Div"),
        ("jumbotron", "Jumbotron"),
        ("row", "Row"),
    ], required=False)
    dimensions = DimensionBlock(required=False, closed=True)
    background = ImageChooserBlock(required=False, closed=True)
    style = LayoutStyleBlock(required=False, closed=True)

    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
    ], required=False, closed=True)

    class Meta:
        icon = "grip"
        template = "components/layout_block.html"
        group = "Containers"

class LayoutBlock2(blocks.StructBlock):

    container_type = blocks.ChoiceBlock([
        ("", "Div"),
        ("jumbotron", "Jumbotron"),
        ("row", "Row"),
    ], required=False)
    dimensions = DimensionBlock(required=False, closed=True)
    background = ImageChooserBlock(required=False, closed=True)
    style = LayoutStyleBlock(required=False, closed=True)

    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
        ("layout", LayoutBlock3(required=False, closed=True)),
    ], required=False, closed=True)

    class Meta:
        icon = "grip"
        template = "components/layout_block.html"
        group = "Containers"

class LayoutBlock(blocks.StructBlock):

    container_type = blocks.ChoiceBlock([
        ("", "Div"),
        ("jumbotron", "Jumbotron"),
        ("row", "Row"),
    ], required=False)
    dimensions = DimensionBlock(required=False, closed=True)
    background = ImageChooserBlock(required=False, closed=True)
    style = LayoutStyleBlock(required=False, closed=True)

    content = blocks.StreamBlock([
        ("title", TitleBlock(required=False, closed=True)),
        ("paragraph", RichTextBlock(required=False, closed=True)),
        ("quote", QuoteBlock(required=False, closed=True)),
        ("html", blocks.RawHTMLBlock(required=False, closed=True)),
        ("image", ImageBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
        ("layout", LayoutBlock2(required=False, closed=True)),
    ], required=False, closed=True)

    class Meta:
        icon = "grip"
        template = "components/layout_block.html"
        group = "Containers"

class CarouselBlock(blocks.StructBlock):

    cycle = blocks.IntegerBlock(min_value=0, max_value=60000, required=False, closed=True)
    display_controls = blocks.BooleanBlock(required=False, closed=True)
    display_indicators = blocks.BooleanBlock(required=False, closed=True)
    content = blocks.ListBlock(
        ImageBlock(closed=True),
        required=False, closed=True)

    style = CarouselStyleBlock(required=False, closed=True)

    class Meta:
        icon = "order"
        template = "components/carousel_block.html"
        group = "Containers"