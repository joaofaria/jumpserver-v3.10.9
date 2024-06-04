from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.const import FileNameConflictResolution


class BasicSerializer(serializers.Serializer):
    file_name_conflict_resolution = serializers.ChoiceField(
        FileNameConflictResolution.choices, default=FileNameConflictResolution.REPLACE,
        required=False, label=_('Resolução de conflitos de nome de arquivo')
    )
    terminal_theme_name = serializers.CharField(
        max_length=128, required=False, default='Padrão',
        label=_('Nome do tema do terminal')
    )


class KokoSerializer(serializers.Serializer):
    basic = BasicSerializer(required=False, label=_('Básico'))
