from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    """ Project Initialization """

    # second commit and push
    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"