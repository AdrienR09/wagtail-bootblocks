from wagtail.core import blocks

class WidthChooserBlock(blocks.ChoiceBlock):
    choices = [
        ("w-auto", "auto"),
        ("w-25", "25%"),
        ("w-50", "50%"),
        ("w-75", "75%"),
        ("w-100", "100%"),
    ]

    class Meta:
        icon = "arrow-down"

class HeightChooserBlock(blocks.ChoiceBlock):
    choices = [
        ("h-auto", "auto"),
        ("h-25", "25%"),
        ("h-50", "50%"),
        ("h-75", "75%"),
        ("h-100", "100%"),
    ]

    class Meta:
        icon = "arrow-up"

class SizeBlock(blocks.StructBlock):

    height = HeightChooserBlock(required=False, closed=True)
    width = WidthChooserBlock(required=False, closed=True)

    class Meta:
        icon = "arrow-up"
        group = "size"
        template = "utilities/size/size_block.html"

class DimensionBlock(blocks.StructBlock):
    height = blocks.IntegerBlock(min_value=1, max_value=500, required=False)
    width = blocks.IntegerBlock(min_value=1, max_value=500, required=False)

    class Meta:
        icon = "arrows-up-down"
        template = "utilities/size/size_block.html"
        group = "size"