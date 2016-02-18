from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class HomePage(Page):
    subpage_types = ['BlogIndexPage']
    pass


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    indexed_fields = ('intro', )
    search_name = "Blog"
    subpage_types = ['BlogPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]


class BlogPage(Page):
    body = RichTextField(blank=True, help_text="Body of the Post")
    date = models.DateField("Post date")
    feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subpage_types = []
    indexed_fields = ('body', )
    search_name = "Blog Entry"

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
        FieldPanel('date'),
    ]
