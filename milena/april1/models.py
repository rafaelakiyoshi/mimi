from __future__ import unicode_literals

from django.db import models


class Tips(models.Model):
    chances = models.IntegerField(default=3)
