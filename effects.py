from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# Chooser blocks :

class ParticlesBlock(blocks.StructBlock):
    
    id = blocks.CharBlock(required=True, closed=True)

    class Meta:
        template = "effects/particles_block.html"