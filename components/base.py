from wagtail.core import blocks

from ..utilities.style import *

class BaseBlock(blocks.StructBlock):

    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "components/base/base_block.html"
        icon = "pill"

class ButtonBaseBlock(blocks.StructBlock):

    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = ButtonStyleBlock(closed=True, required=False)

    class Meta:
        template = "components/base/button_base_block.html"
        icon = "pill"

class InputBaseBlock(blocks.StructBlock):

    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "components/base/input_base_block.html"
        icon = "pill"

class ContainerBaseBlock(blocks.StructBlock):

    background = BackgroundBlock(closed=True, required=False)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "components/base/container_base_block.html"
        icon = "doc-full-inverse"

class SelectBaseBlock(blocks.StructBlock):

    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "components/base/select_base_block.html"
        icon = "doc-full-inverse"

class ListBaseBlock(blocks.StructBlock):

    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)
    items_parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    items_style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "components/base/list_base_block.html"
        icon = "doc-full-inverse"

class NavbarBaseBlock(blocks.StructBlock):

    expand = BreakpointChooserBlock(required=False, closed=True)
    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)
    nav = ContainerBaseBlock(closed=True, required=False)

    class Meta:
        template = "components/base/navbar_base_block.html"
        icon = "doc-full-inverse"

class FormBaseBlock(blocks.StructBlock):

    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(closed=True, required=False)

    class Meta:
        template = "components/base/form_base_block.html"
        icon = "doc-full-inverse"

class ImageBaseBlock(blocks.StructBlock):

    parameters = blocks.StreamBlock([
        ("parameter", blocks.RawHTMLBlock(closed=True, required=False))
        ], closed=True, required=False)
    style = StyleBlock(required=False, closed=True)

    class Meta:
        template = "components/base/image_base_block.html"
        icon = "image"