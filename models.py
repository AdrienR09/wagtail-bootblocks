from django.db import models
from django.utils.translation import gettext as _

from wagtail.core.models import Page
from wagtail.utils.decorators import cached_classmethod
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.core.blocks import StreamBlock, RawHTMLBlock

from mysite.settings import base
from bootblocks import theme, blocks, effects


class AbstractBlockPage(Page):
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
            ("section", blocks.SectionBlock(required=False, closed=True)),
            ("aside", blocks.AsideBlock(required=False, closed=True)),
            ("footer", blocks.FooterBlock(required=False, closed=True)),

            ("modal", blocks.ModalBlock(required=False, closed=True)),
            ("container", blocks.ContainerBlock(required=False, closed=True)),
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

    class Meta:
        abstract = False

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

    @cached_classmethod
    def get_edit_handler(cls):
        edit_handler = TabbedInterface([
            ObjectList(cls.content_panels, heading=_("Content")),
            ObjectList(Page.promote_panels, heading=_("Promote")),
            ObjectList(Page.settings_panels, heading=_("Settings")),
            ObjectList(cls.theme_panels, heading=_("Theme")),
            ObjectList(cls.script_panels, heading=_("Script")),
        ])
        return edit_handler.bind_to(cls)

    class Meta:
        abstract = True

class BlockPage(AbstractBlockPage):
    """
    Block page models attached to the bootblocks module has a startup page to build faster
    website with streamfield.
    """
    pass