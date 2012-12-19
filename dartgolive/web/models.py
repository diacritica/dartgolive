# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False,
        verbose_name=_('Complete name'))
    
    description = models.TextField(max_length=100, blank=False, null=False,
        verbose_name=_('Description'))

    getURI = models.URLField(blank=True, null=True, verbose_name=_('URI to GET'))

    redirectURI = models.URLField(blank=True, null=True, verbose_name=_('URL to REDIRECT'))

    delay = models.IntegerField(blank=True, null=True, verbose_name=_('Delay between GET and REDIRECT (seconds)'))

    active = models.BooleanField(blank=True, verbose_name=_('This is the active project'))

    def __unicode__(self):
        return unicode("%s" % (self.name,))

    class Meta:
        db_table = u'project'
        verbose_name = _(u'Project')
        get_latest_by = 'id'
        ordering = ['id']

    def save(self, *args, **kwargs):

        if self.active:
            activeprojects = Project.objects.filter(active=True)
            for ap in activeprojects:
                ap.active = False
                super(Project, ap).save(*args, **kwargs)

            self.active = True
        super(Project, self).save(*args, **kwargs)
