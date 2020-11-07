from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from django.db import models

from bootblocks.style import *

DEFAULT = None
CERULEAN = "cerulean"
DARKLY = "darkly"
LITERA = "litera"
MATERIA = "materia"
SANDSTONE = "sandstone"
SLATE = "slate"
SUPERHERO = "superhero"
COSMO = "cosmo"
FLATLY = "flatly"
LUMEN = "lumen"
MINTY = "minty"
SIMPLEX = "simplex"
SOLAR = "solar"
UNITED = "united"
CYBORG = "cyborg"
JOURNAL = "journal"
LUX = "lux"
PULSE = "pulse"
SKETCHY = "sketchy"
SPACELAB = "spacelab"
YETI = "yeti"

theme_choices = [
    (DEFAULT ,"default"),
    (CERULEAN ,"cerulean"),
    (DARKLY ,"darkly"),
    (LITERA ,"litera"),
    (MATERIA ,"materia"),
    (SANDSTONE ,"sandstone"),
    (SLATE ,"slate"),
    (SUPERHERO ,"superhero"),
    (COSMO ,"cosmo"),
    (FLATLY ,"flatly"),
    (LUMEN ,"lumen"),
    (MINTY ,"minty"),
    (SIMPLEX ,"simplex"),
    (SOLAR ,"solar"),
    (UNITED ,"united"),
    (CYBORG ,"cyborg"),
    (JOURNAL ,"journal"),
    (LUX ,"lux"),
    (PULSE ,"pulse"),
    (SKETCHY ,"sketchy"),
    (SPACELAB ,"spacelab"),
    (YETI ,"yeti"),
]

class FontBlock(blocks.StructBlock):

    font=blocks.CharBlock(required=False, closed=True)
    name=FontChooserBlock(required=False, closed=True)

    class Meta:
        template = "theme/font_block.html"

class ColorBlock(blocks.StructBlock):

    color = blocks.CharBlock(required=False, closed=True, max_length=12)
    name = ColorChooserBlock(required=False, closed=True)

    class Meta:
        template = "theme/color_block.html"

class BackgroundBlock(blocks.StructBlock):

    color = blocks.CharBlock(required=False, closed=True, max_length=6)
    image = ImageChooserBlock(required=False, closed=True)

    class Meta:
        template = "theme/background_block.html"

class ExtraCSSBlock(blocks.StructBlock):

    code = blocks.RawHTMLBlock(required=False, closed=True)

    class Meta:
        template = "theme/extra_css_block.html"


