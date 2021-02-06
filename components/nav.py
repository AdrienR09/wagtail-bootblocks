from wagtail.core import blocks

from .base import *
from .text import *
from .media import *
from .form import *

class NavLinkBlock(blocks.StructBlock):

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

class NavBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices=[
                ("navbar-nav", "Nav"),
                ("nav pills", "Pills"),
                ("breadcrumb", "Breadcrumb"),
                ("pagination", "Pagination"),
    ], required=False, closed=True)
    nav = blocks.StreamBlock([
        ("navlink", NavLinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
    ], required=False, closed=True)

    class Meta:
        template = "components/nav/nav_block.html"
        icon = "arrow-right-big"
        group = "Navs"

class NavbarBlock(blocks.StructBlock):

    type = blocks.ChoiceBlock(choices=[
                ("", "None"),
                ("navbar-light", "Light"),
                ("navbar-dark", "Dark"),
    ], required=False, closed=True)
    brand = blocks.StreamBlock([
        ("logo", ImageBlock(required=False, closed=True)),
        ("title", TitleBlock(required=False, closed=True)),
    ], required=False, closed=True)
    nav = blocks.StreamBlock([
        ("nav", NavBlock(required=False, closed=True)),
        ("button", ButtonBlock(required=False, closed=True)),
        ("navlink", NavLinkBlock(required=False, closed=True)),
        ("dropdown", DropdownButtonBlock(required=False, closed=True)),
        ("text", RichTextBlock(required=False, closed=True)),
    ], required=False, closed=True)
    block = NavbarBaseBlock(required=False, closed=True)

    class Meta:
        template = "components/nav/navbar_block.html"
        icon = "arrow-up-big"