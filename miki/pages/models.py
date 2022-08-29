from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Page(models.Model):
    """ Page model """

    title = models.CharField(_("Title"), max_length=256)
    content = models.TextField(_("Content"),null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now_add=True)
    is_published = models.BooleanField(_("Publish?"),default=False)
    linked_page = models.ManyToManyField('self', symmetrical=False, blank=True, help_text=_('Select any other pages that this page follows up on.'), related_name='linked_pages')

    def releated_pages(self):
        links = self.linked_page.filter(is_published=True).exclude(id__exact=self.id)
        return links

    def get_absolute_url(self):
        return reverse("pages:detail", args=(self.id,))

    class Meta:
        ordering = ("title",)
        

    def __str__(self):
        return self.title

