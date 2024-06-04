import json

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.const import (
    RDPResolution, RDPSmartSize, KeyboardLayout,
    RDPClientOption, AppletConnectionMethod, RDPColorQuality,
)


class MultipleChoiceField(serializers.MultipleChoiceField):

    def to_representation(self, keys):
        if isinstance(keys, str):
            keys = json.loads(keys)
        return keys

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return json.dumps(list(data))


class BasicSerializer(serializers.Serializer):
    is_async_asset_tree = serializers.BooleanField(
        required=False, default=True, label=_('Carregamento assíncrono da árvore de ativos')
    )


class GraphicsSerializer(serializers.Serializer):
    rdp_resolution = serializers.ChoiceField(
        RDPResolution.choices, default=RDPResolution.AUTO,
        required=False, label=_('Resolução RDP')
    )
    keyboard_layout = serializers.ChoiceField(
        KeyboardLayout.choices, default=KeyboardLayout.EN_US_QWERTY,
        required=False, label=_('Layout do teclado')
    )
    rdp_client_option = MultipleChoiceField(
        choices=RDPClientOption.choices, default={RDPClientOption.FULL_SCREEN},
        label=_('Opção de cliente RDP'), required=False
    )
    rdp_color_quality = serializers.ChoiceField(
        choices=RDPColorQuality.choices, default=RDPColorQuality.HIGH,
        label=_('Qualidade de cor RDP'), required=False
    )
    rdp_smart_size = serializers.ChoiceField(
        RDPSmartSize.choices, default=RDPSmartSize.DISABLE,
        required=False, label=_('Tamanho inteligente RDP'),
        help_text=_('Determina se o computador cliente deve dimensionar o conteúdo no computador'
                    'remoto para ajustar-se ao tamanho da janela do computador cliente quando a janela for redimensionada.')
    )
    applet_connection_method = serializers.ChoiceField(
        AppletConnectionMethod.choices, default=AppletConnectionMethod.WEB,
        required=False, label=_('Método de conexão de aplicativo remoto')
    )


class CommandLineSerializer(serializers.Serializer):
    character_terminal_font_size = serializers.IntegerField(
        default=14, min_value=1, max_value=9999, required=False,
        label=_('Tamanho da fonte do terminal'),
    )
    is_backspace_as_ctrl_h = serializers.BooleanField(
        required=False, default=False, label=_('Backspace como Ctrl+H')
    )
    is_right_click_quickly_paste = serializers.BooleanField(
        required=False, default=False, label=_('Clique com o botão direito e cole rapidamente')
    )


class LunaSerializer(serializers.Serializer):
    basic = BasicSerializer(required=False, label=_('Básico'))
    graphics = GraphicsSerializer(required=False, label=_('Visualização'))
    command_line = CommandLineSerializer(required=False, label=_('Linha de comando'))
