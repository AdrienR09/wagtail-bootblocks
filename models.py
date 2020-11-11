from django.db import models
from django.utils.translation import gettext as _

from wagtail.core.models import Page
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.blocks import StreamBlock, RawHTMLBlock
from bootblocks import theme, blocks, effects

class BlockPage(Page):
    """
    Block page models attached to the bootblocks module has a startup page to build faster
    website with streamfield.
    """

    template = "page/block_page.html"

    theme_label = models.CharField(max_length=20, choices=theme.theme_choices, null=True, blank=True)
    extra_theme = StreamField(
        [
            ("font", theme.FontBlock(closed=True)),
            ("color", theme.ColorBlock(closed=True)),
            ("background", theme.BackgroundBlock(closed=True)),
            ("extra_css", theme.ExtraCSSBlock(closed=True)),
        ],
        null=True,
        blank=True,
    )

    body = StreamField(
        [
            ("header", blocks.HeaderBlock(closed=True)),
            ("main", blocks.MainBlock(closed=True)),
            ("footer", blocks.FooterBlock(closed=True)),
        ],
        null=True,
        blank=True,
    )

    extra_js = StreamField(
        [
            ("script", RawHTMLBlock(closed=True)),
            ("particles", effects.ParticlesBlock(closed=True)),
        ],
        null=True,
        blank=True,
    )

    theme_panels = Page.content_panels + [
        FieldPanel("theme_label"),
        FieldPanel("extra_theme"),
    ]

    content_panels = [
        StreamFieldPanel("body"),
    ]

    script_panels = [
        StreamFieldPanel("extra_js"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=_("Content")),
        ObjectList(Page.promote_panels, heading=_("Promote")),
        ObjectList(Page.settings_panels, heading=_("Settings")),
        ObjectList(theme_panels, heading=_("Theme")),
        ObjectList(script_panels, heading=_("Script")),
    ])