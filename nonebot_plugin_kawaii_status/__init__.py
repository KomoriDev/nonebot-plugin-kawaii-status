"""运行状态"""

from nonebot import require
from nonebot.rule import Rule
from nonebot import get_plugin_config
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import Command
from nonebot_plugin_alconna import __plugin_meta__
from nonebot_plugin_alconna.uniseg import UniMessage

from .config import Config

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="运行状态",
    description="NoneBot2 服务器状态查看插件",
    usage="/status",
    type="application",
    homepage="https://github.com/KomoriDev/nonebot-plugin-kawaii-status",
    config=Config,
    supported_adapters=__plugin_meta__.supported_adapters,
    extra={
        "unique_name": "KaWaii Status",
        "example": "/status",
        "author": "Komorebi <mute231010@gmail.com>",
        "version": __version__,
    },
)

from .drawer import draw

config = get_plugin_config(Config).status

def to_me() -> Rule:
    if config.to_me:
        from nonebot.rule import to_me
        return to_me()

    async def _to_me() -> bool:
        return True

    return Rule(_to_me)

status = (
    Command("status", help_text="查看林汐运行状态")
    .usage("/status\n/状态")
    .action(lambda: UniMessage.image(raw=draw()))
    .build(
        rule=to_me(),
        aliases={"状态"},
        use_cmd_start=True,
        permission=SUPERUSER if config.only_superuser else None,
    )
)

