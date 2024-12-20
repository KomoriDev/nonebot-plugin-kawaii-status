from pydantic import Field, BaseModel
from nonebot.plugin import get_plugin_config


class ScopedConfig(BaseModel):
    only_superuser: bool = Field(default=False)
    """是否只能由 SUPERUSER 触发指令"""
    to_me: bool = Field(default=False)
    """触发指令是否需要 @Bot"""


class Config(BaseModel):
    status: ScopedConfig = Field(default_factory=ScopedConfig)
    """Kawaii Status Config"""


config: ScopedConfig = get_plugin_config(Config).status
