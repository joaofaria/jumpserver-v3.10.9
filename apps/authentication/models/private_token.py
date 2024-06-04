from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class PrivateToken(Token):
    """Inherit from auth token, otherwise migration is boring"""
    date_last_used = models.DateTimeField(null=True, blank=True, verbose_name=_('Usado pela última vez em'))

    class Meta:
        verbose_name = _('Token privado')
